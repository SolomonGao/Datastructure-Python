from simple_stack import Stack

badminton_tube = [4, 3, 5, 6, 2, 8, 7]

def find_pair(array):
    stack = Stack()
    size = len(array)
    result = []

    for i in range(size - 1):
        if stack.size() == 0:
            stack.push(badminton_tube[i])

        if  stack.peek() <= badminton_tube[i + 1]:
                stack.push(badminton_tube[i + 1])
        else:
            result.append(i + 2)
    print("These badmintons are in the wrong order:")        
    print(result)

find_pair(badminton_tube)