class Node:
    
    def __init__(self, data = 0):
        self.data = data
        self.left = None
        self.right = None 
        self.parent = None

class BinaryTree:
    
    def construct_trees(self, pre, size):
        root = Node(pre[0])
        
        s = []
        s = s.append(root)

        i = 1

        while(size > i):
            temp = None

            while (len(s) > 0 and pre[i] > s[-1].data):  
                temp = s.pop()