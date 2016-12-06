class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkList:
    temp = None
    def __init__(self):
        self.head = None

    def add(self,item):
        global temp
        if not self.head:
            temp = Node(item)
            self.head = temp
        else:
            a = temp
            temp = Node(item)
            a.setNext(temp)
        temp.setNext(None)

    def getall(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

mylist = LinkList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

mylist.getall()
