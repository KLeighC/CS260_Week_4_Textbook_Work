#Stack abstract data type
#Structure and Operations

#Stack() creates new empty stack
#push(item) adds new item to the top of the stack
#pop() removes top item from the stack, returns the item
#peek() returns top item from the stack but does not remove it
#isEmpty() tests to see whether the stack is empty, returns a boolean value
#size() returns number of items on the stack, returns an integer

#Implementing a stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

"""
m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
m.peek()
print(m.peek())


m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.isEmpty():
    m.pop()
    m.pop()
print(m.peek())
"""