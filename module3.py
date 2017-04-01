import pickle
class BOOK:
    def __init__(self):
        self.Bno=0
        self.Name=""
        self.Author=""
        self.BSP=0
    def get_data(self):
        self.Bno=input("Enter the book number")
        self.Name=raw_input("Enter name of book")
        self.Author=raw_input("Enter author")
        self.BSP=raw_input("Enter the basic selling price")
    def revenue(self,):
        d=input("Enter number of days "+self.Name+" was kept")
        print self.BSP
        rev=0.02*int(self.BSP)
        if d>7:
            rev+=(d-7)*2
        return rev
    def showdata(self):
        print "Book No:",self.Bno
        print "Book Name:",self.Name
        print "Author:",self.Author
        print "Price:",self.BSP
while True:
    choice=input("Enter 1 to append a book in the library, 2 to display a report for all the books, 3 to exit")
    if choice==1:
        myfile=open("lib.dat","wb+")
        b=BOOK()
        while True:
            b.get_data()
            pickle.dump(b,myfile)
            a=raw_input("Enter y to add more, n to exit")
            if a.lower()=="n":
                break
        myfile.close()
    elif choice==2:
        try:
            myfile=open("lib.dat","rb")
            while True:
                b=pickle.load(myfile)
                r=b.revenue()
                b.showdata()
                print "Revenue:",r
            myfile.close()
        except EOFError:
            pass
        except IOError:
            print "File not found"
    elif choice==3:
        break