class stack():
    def __init__ (self):
        self.elements=[]
    def push(self,data):
        self.elements.append(data)
    def pop(self):
        return self.elements.pop()
stack=stack()
print("\n The initial view of stack",stack.__dict__)
stack.push(3)
stack.push('test')
print("\n The current view of the stack",stack.__dict__)
print("\n The popped out element from the stack",stack.pop())
print("\n The current view of the stack",stack.__dict__)
print("\n The popped out element from the stack",stack.pop())
print("\n The final view of the stack",stack.__dict__)
