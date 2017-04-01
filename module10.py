class AdmissionQueue:
    q=[]
    def __init_(self):
        self.reg_no=0
        self.Name=""
        self.admission_to_class=""
    def enqueue(self):
        self.reg_no=input("Enter reg number")
        self.Name=raw_input("Enter name")
        self.admission_to_class=raw_input("Enter the class you want admission to (Nursery,KG,1)")
        info=[self.reg_no,self.Name,self.admission_to_class]
        AdmissionQueue.q.append(info)
        print "Entry is added"
    def display(self):
        print "Number of admissions is",len(AdmissionQueue.q)
    def report(self):
        n=0
        k=0
        f=0
        o=0
        for char in AdmissionQueue.q:
            if char[2].upper()=="NURSERY":
                n+=1
            elif char[2].upper()=="KG":
                k+=1
            elif char[2]=="1":
                f+=1
            else:
                o+=1
        print "Nursery:",n
        print "KG:",k
        print "First:",f
        print "Others:",o
qu=AdmissionQueue()
while True:
    choice=input("Enter 1 to add an admission,2 to display number of admissions, 3 to print number of applications per class, 4 to exit")
    if choice==1:
        qu.enqueue()
    elif choice==2:
        qu.display()
    elif choice==3:
        qu.report()
    elif choice==4:
        print "Exit"
        break
