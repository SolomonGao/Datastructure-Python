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

## Implementation
Stack is very easy in python. It can be created by simplily using array.

* pop
```python
stack = [1,2,3,4,5] # create a stack
stack.pop() # pop out 5 from the stack
# [1,2,3,4]
```
* push
```python
stack.append(6) # push 6 to the stack
[1,2,3,4,6]
```
* size
```python
size = len(stack) # 5
```
* empty
```python
if stack: # if stack is not empty
   doSomething()
```
* top
```python
stack[-1] # 6
```
Or if you want to create a class for stack, try yourself first and there is an sample you can check it out.
Example solution: [stack](simple_stack.py)

Then use this stack to slove these problem below!
## Example
Stack is good at tracking history. Like it's name, 
if you want to process some data like stacking blocks, you can use stack.
1. Now we have a badminton tube with 8 shuttlecocks numbered 1 to 8 in it. Now we want to put these shuttlecocks upside down and put them in the barrel. Try using stack for this task.

Template: [reverse](reverse.py)
Solution: [reverse solution](reverse_solution.py)

## Problem to solve

Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 

1. For an array, the rightmost element always has the next greater element as -1.
2. For an array that is sorted in decreasing order, all elements have the next greater element as -1.
3. For the input array [4, 5, 2, 25], the next greater elements for each element are as follows.

Element |  NGE
--------|------
   4    |  5
   5    |  25
   2    |  25
   25   | -1

Template: [next greater element](NGE.py)
### Solution
Please try yourself first before seeing the solution.
[Sample solution](stack_example.py)