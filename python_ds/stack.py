# LIFO

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, dataval):
        self.dataval = dataval
        if self.dataval not in self.stack:
            self.stack.append(self.dataval)
            return True
        else:
            return False
        
    def peek(self):     
	    return self.stack[-1]
    
    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

if __name__ == "__main__":
    S = Stack()
    S.push("Mon")  
    S.push("Tue")
    print(S.peek())
    S.push("Wed")  
    S.push("Thu")
    print(S.peek())
    S.push("Fri")
    print(S.pop())
