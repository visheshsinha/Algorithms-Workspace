class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def traverse(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def insertBegin(self, newData):
        NewNode = Node(newData)
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    def insertEnd(self, newData):
        NewNode = Node(newData)

        if self.headval is None:
            self.headval = NewNode
            return
        
        lastNode = self.headval

        while(lastNode.nextval):
            lastNode = lastNode.nextval
        
        lastNode.nextval = NewNode

    def insertAfter(self, afterNode, newData):
        if afterNode is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newData)
        NewNode.nextval = afterNode.nextval
        afterNode.nextval = NewNode
    
    def deleteNode(self, remove):
        head = self.headval
        if (head is not None):
            if (head.dataval == head):
                self.head = head.nextval
                head = None
                return
        
        while (head is not None):
            if head.dataval == remove:
                break
            prev = head
            head = head.nextval
        
        if (head == None):
            return

        prev.nextval = head.nextval
        head = None
                
if __name__ == "__main__":
    List1 = SLinkedList()
    List1.headval = Node("Mon")

    e2 = Node("Tue")
    e3 = Node("Wed")

    List1.headval.nextval = e2
    e2.nextval = e3

    List1.insertBegin("Sun")
    List1.insertEnd("Fri")

    List1.insertAfter(List1.headval.nextval.nextval.nextval, "Thu")

    List1.traverse()

    List1.deleteNode("Mon")
    print()
    List1.traverse()

