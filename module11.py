class LIST:
    def __init__(self):
        self.l=[]
    def create(self):
        n=input("Enter length of list")
        for i in range(n):
            a=input("Enter")
            self.l.append(a)
    def display(self):
        print "List:",
        for char in self.l:
            print char,
        print
    def bubblesort(self):
        for i in range(len(self.l)-1):
            for j in range(len(self.l)-i-1):
                if self.l[j]>self.l[j+1]:
                    self.l[j],self.l[j+1]=self.l[j+1],self.l[j]
            print "List after ",i+1, " iteration = ",self.l
    def linearsearch(self,n):
        if len(self.l)==0:
            print "Empty list"
        else:
            for i in range(len(self.l)):
                if i==n:
                    avail=1
                    pos=i+1
                    break
                else:
                    avail=0
            if avail==1:
                print "Item found at pos",pos
            else:
                print "Item not found"
    def binarysearch(self,n):
        if len(self.l)==0:
            print "Empty List"
        else:
            self.l.sort()
            first=0
            last=len(self.l)-1
            avail=0
            while first<=last:
                midpoint = (first + last)/2
                if self.l[midpoint]==n:
                    pos=midpoint
                    avail=1
                    break
                elif n<self.l[midpoint]:
                        last=midpoint-1
                else:
                    first = midpoint+1
            if avail==1:
                print "Item found at pos",pos
            else:
                print "Item not found"
    def mergesort(self,newl):
        mlist=[]
        newl.sort()
        i=0
        j=0
        while i<len(self.l) and j<len(newl):
            if self.l[i]<newl[j]:
                mlist.append(self.l[i])
                i+=1
            elif self.l[i]>newl[j]:
                mlist.append(newl[j])
                j+=1
        while i<len(self.l):          #if a list has more elements than other
            mlist.append(self.l[i])
            i+=1
        while j<len(newl):
            mlist.append(newl[j])
            j+=1
        print "New list:",mlist