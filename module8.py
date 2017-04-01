import pickle
class PHONE:
    def __init__(self):
        self.Phoneno=0
        self.AreaCode=""
        self.Name=""
    def get_data(self):
        self.Phoneno=input("Enter phone number")
        self.AreaCode=raw_input("Enter code")
        self.Name=raw_input("Enter name")
    def display_data(self):
        print "Number:", self.Phoneno
        print "Code:", self.AreaCode
        print "Name:", self.Name
    def match(self):
        if self.AreaCode.upper()=="DEL":
            return 0
        else:
            return 1
def Ptransfer_detail():
        try:
            myfile=open("phone.dat","rb")
            newfile=open("PHONEBACK.dat","wb")
            while True:
                p=pickle.load(myfile)
                print p
                if p.match()==0:
                    print 1
                    pickle.dump(p,newfile)
                else:
                    pass
            myfile.close()
            newfile.close()
        except EOFError:
            pass
        except IOError:
            print "File not found"
while True:
    choice=input("Enter 1 to add information to the file, 2 to display the contents of the file, 3 to copy data with code DEL to a new file,4 to exit")
    if choice==1:
        myfile=open("phone.dat","ab+")
        p=PHONE()
        while True:
            p.get_data()
            pickle.dump(p,myfile)
            a=raw_input("Enter y to add more, n to exit")
            if a.lower()=="n":
                break
        myfile.close()
    elif choice==2:
        try:
            myfile=open("phone.dat","rb")
            while True:
                p=pickle.load(myfile)
                p.display_data()
            myfile.close()
        except EOFError:
            pass
        except IOError:
            print "File not found"
    elif choice==3:
        Ptransfer_detail()
    elif choice==4:
        break