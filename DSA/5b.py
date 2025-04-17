class Queue:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def enqueue(self,items):
        self.items.insert(0,items)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print("The size of the queue after inserting some elements",q.size())
