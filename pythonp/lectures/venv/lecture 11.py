#DATA STRUCTURES
#STACK
class Stack:
    def __init__(self):
        self.data = []

    def push(self,val):
        self.data.append(val)

    def pop(self):
        return  self.data.pop()

    def __str__(self):
        return str(self.data)

    def getSize(self):
        return str(self.data)

    def isEmpty(self):
        return len(self.data)==0

    def top(self):
        return self.data[-1]

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

s1= Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
# print(s1)
# print(s1.pop())
# print(s1)
# print(s1.getSize())
# print(s1.isEmpty())
# print(len(s1))

s2= Stack()
s2.push(10)
#print(s2)

#QUEUE
class Node:
    def __init__(self,val):
        self.val= val
        self.next = None

class Queue:
    def __init__(self):
        self.start=None
        self.end = None
        self.count= 0

    def enqueue(self,val):
        newNode = Node(val)
        if self.end ==None:
            self.start = newNode
            self.end = newNode
        else:
            self.end.next = newNode
            self.end = newNode
        self.count +=1


    def dequeue(self):
        if self.start ==None:
            return
        elif self.start== self.end:
            self.start = None
            self.end =None
        else:
            self.start = self.start.next
        self.count -=1

    def getSize(self):
        return self.count

    def front(self):
        if self.start == None:
            return None
        return self.start.val

    def isEmpty(self):
        return self.count ==0




    def __str__(self):
        s = ''
        currNode = self.start
        while currNode != None:
            s+= str(currNode.val) + '-> '
            currNode = currNode.next
        return s

q1= Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.dequeue()
print(q1)
print(q1.getSize())

