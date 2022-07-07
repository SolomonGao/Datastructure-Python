# prints element and NGE pair for all
# elements of array[] of size length(array)
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
        pass # start right here