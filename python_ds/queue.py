# FIFO

class Queue:
    def __init__(self):
        self.queue = list()
    
    def insertQ(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        else:
            return False
    
    def removeQ(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return False


    def traverseQ(self):
        print(self.queue, len(self.queue))
    
if __name__ == "__main__":
    Q = Queue()
    Q.insertQ("Mon")
    Q.insertQ("Mon")
    Q.insertQ("Tue")

    Q.traverseQ()
    
    Q.insertQ("Wed")
    Q.insertQ("Thu")

    Q.traverseQ()
    
    print('Removed', Q.removeQ())




