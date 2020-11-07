class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def append(self, dataval):
        newNode =Node(dataval)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
        
        last = self.head
        while last.next != None:
            last = last.next
        
        last.next = newNode
        newNode.prev = last
        return
    
    def traverse(self, node):
      while (node is not None):
            print(node.data),
            last = node
            node = node.next
    
if __name__ == "__main__":
    dLL = DoubleLinkedList()
    
    dLL.push("Mon")
    dLL.push("Tue")
    dLL.push("Wed")

    dLL.traverse(dLL.head)
    print()
    dLL.insert(dLL.head.next, "Thu")
    dLL.traverse(dLL.head)

    print()
    dLL.append("Fri")
    dLL.traverse(dLL.head)