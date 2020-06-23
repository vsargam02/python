#tree

class Node:
    def __init__(self,val):
        self.val=val
        self.left =None
        self.right= None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,val):
        newNode = Node(val)
        if self.root==None:
            self.root= newNode
        else:
            self._insert(self.root,newNode)


    def _insert(self,startNode,newNode):
        if startNode.val == newNode.val :       # .val for compare the values
            return
        elif startNode.val < newNode.val:
            if startNode.right == None:
                startNode.right = newNode
            else:
                self._insert(startNode.right,newNode)
        else:
            if startNode.left == None:
                startNode.left = newNode
            else:
                self._insert(startNode.left,newNode)

    def printDF(self):
        self._printDF(self.root)


    def _printDF(self,startNode):
        if startNode == None:
            return
        self._printDF(startNode.left)
        print(startNode.val)
        self._printDF(startNode.right)

    def printBF(self):
        q = []
        q.append(self.root)
        while len(q)!= 0:
            n = q.pop(0)
            if n != None:
                print(n.val)
                q.append(n.left)
                q.append(n.right)

    def search(self,val):
        return self._search(self.root,val)


    def _search(self,startNode,val):         # recursive
        if startNode == None:
            return False
        if startNode.val == val:
            return True
        elif startNode.val<val:
            return self._search(startNode.right,val)
        else:
            return self._search(startNode.left,val)

t1 =BST()
t1.insert(5)
t1.insert(7)
t1.insert(6)
t1.insert(3)
t1.insert(9)
t1.insert(1)
t1.insert(4)
#t1.printBF()
print(t1.search(4))
print(t1.search(10))


 














