# Create your stack!


class Stack():

    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

    def push(self, datum):
        self.stack.append(datum)

    def pop(self):
        if stack.size() > 0:
            return self.stack.pop()
        else:
            return "Empty stack"

    def peek(self):
        if stack.size() > 0:
            return self.stack[-1]
        else:
            return "Empty stack"


stack = Stack()
stack.push(1)
stack.push(2)

print("Initial stack:")
print(stack)

stack.push(3)

print("New stack:")
print(stack)

print("The topmost element is:")
print(stack.peek()) # 3

print("The size of this stack is:")
print(stack.size()) # 3

print("Elements popped from stack:")
print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
print("Try to pop from an empty stack:")
print(stack.pop()) # Empty stack

print("Is this stack empty?")
print(stack.empty()) # True