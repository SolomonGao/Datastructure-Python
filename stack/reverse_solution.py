from simple_stack import Stack

badminton_tube = [1,2,3,4,5,6,7,8]

def reverse(array):
    stack = Stack()
    size = len(badminton_tube)
    for i in range(size - 1, -1, -1):
        stack.push(badminton_tube[i])
    
    print(stack)

reverse(badminton_tube)