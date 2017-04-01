class Magic_sq:
    def __init__(self):
        self.N=0
        self.A=[]
    def Readarray(self):
        self.N=input("Enter size of the array")
        self.A=[[0 for i in range(self.N)]for j in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                self.A[i][j]=input()
    def Displayarray(self):
        print "Array:"
        for i in range(self.N):
            for j in range(self.N):
                print self.A[i][j],
            print
    def Ismagic_square(self):
        for i in range(self.N-1):       #check sum of rows
            s=sum(self.A[i])
            s1=sum(self.A[i+1])
            if s==s1:
                sq=1
                s=0
                s1=0
            else:
                sq=0
                break
        for i in range(self.N):          #check sum of columns
            s=0
            s1=0
            for j in range(self.N-1):
                s+=self.A[j][i]
                s1+=self.A[j+1][i]
            if s==s1:
                sq=1
            else:
                sq=0
        for i in range(self.N):          #check sum of diagonals
            j=-1
            diag1+=self.A[i][i]
            diag2+=self.A[i][j]
            j-=1
        print diag1,diag2
        if diag1==diag2:
            sq=1
        else:
            sq=0
        if sq==1:
            print "Yes it is a magic square"
        elif sq==0:
            print "It is not a magic square"
    def Transpose(self):
        T=[[0 for i in range(self.N)]for j in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                T[j][i]=self.A[i][j]
        print "Transpose:"
        for i in range(self.N):
            for j in range(self.N):
                print T[i][j],
            print
c=Magic_sq()
while True:
    choice=input("Enter 1 to create array, 2 to display array,3 to check if it is a magic square, 4 to find its transpose, 5 to exit")
    if choice==1:
        c.Readarray()
    elif choice==2:
        c.Displayarray()
    elif choice==3:
        c.Ismagic_square()
    elif choice==4:
        c.Transpose()
    elif choice==5:
        print "Exit"
        break