class BSTNode(object):
    """Node Unit in a BST """

    def __init__(self, parent, k):
        """k: The key of the node."""

        self.key = k
        self.parent = parent
        self.right = None
        self.left = None

    def find(self, k):
        """Return the node for key k if is in the tree, or None otherwise."""

        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def next_larger(self):

        # Has a right Subtree 
        if self.right is not None:
            return self.right.find_min()
        
        # Doesn't have a right Subtree
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node."""
        
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):

        # When x has atmost 1 child
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is None:
                    self.parent.right.parent = self.parent
            return self

        # When x has 2 children
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

class BST(object):
    
    def __init__(self):
        self.root = None
    
    def find(self, k):
        return self.root and self.root.find(k)
    
    def find_min(self):
        return self.root and self.root.find_min()

    def insert(self, k):
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
    
    def delete(self, k):
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = BSTNode(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()
    
    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()

    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])



class MinBSTNode(BSTNode):
    def __init__(self, parent, k):
        super(MinBSTNode, self).__init__(parent, k)
        self.min = self

def test(args=None, BSTtype=BST):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print('usage: %s <number-of-random-items | item item item ...>') % \
              sys.argv[0]
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in range(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print(tree)
    for item in items:
        tree.insert(item)
        print()
        print(tree)
    

if __name__ == "__main__": test()