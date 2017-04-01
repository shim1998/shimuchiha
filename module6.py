import random
class Queue:
    q=[]
    def enqueue(self):
        n=random.randint(100,999)
        Queue.q.append(n)
        print "Entry is added"
        print "Your order no is",n
    def dequeue(self):
        if len(Queue.q)==0:
            print "Queue empty"
        else:
            val=Queue.q.pop(0)
            print "Order number",val,"is ready"
    def display(self):
        if len(Queue.q)==0:
            print "Queue empty"
        else:
            print "Queue:"
            for i in Queue.q:
                print i
qu=Queue()
while True:
    choice=input("Enter 1 to gen order,2 to display order, 3 to dequeue an order, 4 to exit")
    if choice==1:
        qu.enqueue()
    elif choice==2:
        qu.display()
    elif choice==3:
        qu.dequeue()
    elif choice==4:
        print "Exit"
        break