class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
            laste.nextval=NewNode
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    def search_item(self, x):
        if self.headval is None:
            print("List has no elements")
            return
        n = self.headval
        while n is not None:
            if n.dataval == x:
                print("Item found")
                return True
            n = n.nextval
            print("item not found")
            return False
    def getCount(self):
        temp = self.headval # Initialise temp count = 0 # Initialise count
        while (temp):
            count += 1
            temp = temp.nextval
            return count
    def RemoveNode(self, Removekey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
            while (HeadVal is not None):
                if HeadVal.dataval == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.nextval
                if (HeadVal == None):
                    return
                prev.nextval = HeadVal.nextval
                HeadVal = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
list = SLinkedList()
list.headval = Node("1")
e2 = Node("2")
e3 = Node("3")
list.headval.nextval = e2
e2.nextval = e3
list.AtBegining("4")
list.AtEnd("5")
list.Inbetween(list.headval.nextval,"6")
list.search_item("3")
print ("Count of nodes is :",list.getCount())
list.RemoveNode("2")
list.listprint()