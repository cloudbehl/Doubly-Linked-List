class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prv = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getprev(self):
        return self.prv

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setprev(self,newprv):
        self.prv = newprv

class DoublyLinkList:
    temp = None
    def __init__(self):
        self.head = None

    def add(self,item):
        global temp
        if not self.head:
            temp = Node(item)
            temp.setprev(None)
            self.head = temp
        else:
            a = temp
            temp = Node(item)
            temp.setprev(a)
            a.setNext(temp)
        temp.setNext(None)

    def doubley(self):
        current = self.head
        count = 0
        while current != None:
            if current.getData() == 77:
                return (current.getprev().getData(),current.getData(),current.getNext().getData())
            current = current.getNext()

mylist = DoublyLinkList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.doubley())
