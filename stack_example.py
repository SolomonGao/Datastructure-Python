# prints element and NGE pair for all
# elements of arr[] of size n
def printNGE(array):
    size = len(array)
    stack = []
    res = [0 for i in range(size)]
 
    # iterate for rest of the elements
    for i in range(size-1,-1,-1):
 
        # if stack is not empty, then
        # pop an element from stack.
        # If the popped element is smaller
        # than next, then
        # a) print the pair
        # b) keep popping while elements are
        # smaller and stack is not empty
        if (len(stack) != 0):
            while (len(stack) != 0 and stack[-1] <= array[i]):
                stack.pop()
        if len(stack) == 0:
            res[i] = -1 
        else:
            res[i] = stack[-1]
        stack.append(array[i])
    
    print("Element | NGE")
    for i in range(len(array)):
        print(str(array[i]) + " | " + str(res[i]))
     
# Test
array = [5, 10, 7, 21, 3, 18]
printNGE(array)