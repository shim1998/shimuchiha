class Stack:
    s=[]
    def push(self):
        n=raw_input("Enter")
        Stack.s.append(n)
        print "Entry is added"
    def pop(self):
        if len(Stack.s)==0:
            print "Stack empty"
        else:
            val=Stack.s.pop(-1)
            print val,"is removed from the stack"
    def display(self):
        if len(Stack.s)==0:
            print "Stack empty"
        else:
            for i in range(len(Stack.s)-1,-1,-1):
                for char in Stack.s[i]:
                    if char.lower() in ["a","e","i","o","u"]:
                        pass
                    else:
                        print char,
                print
st=Stack()
while True:
    choice=input("Enter 1 to add a string,2 to pop a string, 3 to display stack, 4 to exit")
    if choice==1:
        st.push()
    elif choice==2:
        st.pop()
    elif choice==3:
        st.display()
    elif choice==4:
        print "Exit"
        break