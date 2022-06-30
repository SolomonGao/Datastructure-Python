# Stack Tutorial

## Introduction

As a data structure, a *stack* is a special linear list that can only be inserted and deleted at one end. It stores data on a last in first out basis(LIFO). The data entered first is pushed to the bottom of the stack, and the last data is at the top of the stack. When you need to read data, pop data from the top of the stack (the last data is read first).

## LIFO

Since the stack data structure only allows operations at one end, the stack must follow the last-in, first-out principle.

Here we take the badminton tube as an example. At the beginning, the badminton barrel is empty, that is, the empty stack. Then we put the shuttlecocks one by one (that is, push into the stack). When we need badminton, we take it from the badminton barrel (pop). So the first shuttlecock we got was the one we put in at the end.

![stack_representation](stack_representation.jpg)

## Stack in Python
Stack in Python is very simple. 
The functions associated with stack are:
* empty() – Returns whether the stack is empty – Time Complexity: O(1)
* size() – Returns the size of the stack – Time Complexity: O(1)
* top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
* push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
* pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

## Example
To demostrate how stack works, we first create a stack
```python
class Stack():

    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)
```
This method below returns whether the stack is empty.
#### Empty
```python
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
```
This method returns the size of the stack.
#### Size
```python
    def size(self):
        return len(self.stack)
```
Then we write the push method to let user add element into the stack.
#### Push
```python
    def push(self, datum):
        self.stack.append(datum)
```
#### Pop
Next we write the pop method to allow user to remove element from the stack. Notice that we should write a if statment to determine if the stack is empty.
```python
    def pop(self):
        if stack.size() > 0:
            self.stack.pop()
        else:
            return "Empty stack"
```
#### Peek/Top
This method returns a reference to the topmost element of the stack.
```python
    def peek(self):
        if stack.size() > 0:
            return self.stack[-1]
        else:
            return "Empty stack"
```
#### Test
```python
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
```

#### Output
```python
Initial stack:
[1, 2]
New stack:
[1, 2, 3]
The topmost element is:
3
The size of this stack is:
3
Elements popped from stack:
3
2
1
Try to pop from an empty stack:
Empty stack
Is this stack empty?
True
```
## Problem to Solve
### Create Your Stack Using Class

Create your own stack object and test it out!
You should create these methods for it:
* pop
* push
* size
* empty
* top
(Try not to look at the tutorial above while doing this problem. Make sure you understand how stack work before doing it.)
Example solution: [Solution](simple_stack.py)
### Challange Next Greater Element

Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 

#### Example

1. For an array, the rightmost element always has the next greater element as -1.
2. For an array that is sorted in decreasing order, all elements have the next greater element as -1.
3. For the input array [4, 5, 2, 25], the next greater elements for each element are as follows.

Element |  NGE
--------|------
   4    |  5
   5    |  25
   2    |  25
   25   | -1


#### Solution
Please try yourself first before seeing the solution.
[Sample solution](stack_example.py)