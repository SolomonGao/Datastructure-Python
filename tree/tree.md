# Tree

## Introduction

### Tree
A tree, as its name implies, is a tree-like structure. Much like a linked list, it is also linked by pointers to data together. The difference is that one node of the tree can be connected to many different nodes. Here we will mainly learn about binary trees.

### Binary Tree
A binary tree is a tree in which each node can link at most two other nodes. We call the top node root. The nodes to the left and right of any parent node form a subtree. The nodes with no children are called leaves. A node that has connected nodes is called a parent node. The node connected to the parent are called child nodes.
![tree](tree.png)

### Binary Search Tree
Binary search trees(BST) are numeric and ordered trees. It follows these rules:
1. If its left subtree is not empty, then the value of all nodes in the left subtree is less than the value of its root node.
2. If its right subtree is not empty, then the value of all nodes in the right subtree is greater than the value of its root node.

Using binary search trees, we can quickly sort a bunch of data (as you may have noticed, the process is similar to the binary sorting). Anything bigger than the node is placed on the right, and smaller than it is placed on the left. When we want to read these data, we can quickly find the data we want.
![binary search tree](binary_search_tree.png)

As shown on the left above, when we want to find out whether 3 is in the structure, we first compare 10 and 3. 3 is smaller than 10, so we go to the left of 10 which is 6. Comparing 6 and 3, 3 is smaller than 6, then we go to the left side of 6, which is 3. We found 3. It only take 3 steps to find 3 in 7 elements.

### Balanced Binary Search Tree
A balanced search binary tree is a search binary tree in which the height difference between any two subtrees does not differ significantly. This is also our most widely used tree. Imagine if the root of a tree is the smallest value, and the rest of the values are sorted by size, then the tree will become no different from the linked list. This also loses the significance of the tree.

In the right picture above, it is not a balanced search binary tree.

### BST in Python

Most of the operations of BST need to use recursion, they are more complicated and it takes some time to understand them, but once you understand them, you will find them really convenient.

We will discuss these operations and try to write them by yourself:
1. Insert - Insert a value into the tree.
3. Contain - Determine if a value is in the tree.
5. Traverse forward - Visit all objects from smallest to largest.
6. Traverse backward - Visit all objects from largest to smallest.

We first create a BST class and next we together figure out how to implement those methods.
```python
class BST():
    
    class node():

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
```
#### Insert
The idea is that we use recursion. 

1. Determining recursive function parameters and return values. The parameters we need are the inserted value itself, and a node (from root).
2. Determine the termination conditions. We will stop the recursion when the node has no children. And insert the value into either the node's left or right.
3. Determining the logic of a single level of recursion. When we have a node and a value that we want to insert, we compare the node's value to the size of the value. If the node's value is greater than it, then it goes to the left of the node. Otherwise, go to the right.
```python
def insert(self, data):
        if self.root:
            self._insert(data, self.root)
        else:
            self.root = BST.node(data)

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = BST.node(data)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = BST.node(data)
```
#### Contain
We use the same method to find if the tree contains a value. Just change the termination condition. Returns True when the value of the current node is equal to the searched value. If there are no nodes down, then return False
```python
def __contains__(self, data):
        return self._contains(data, self.root)

    def _contains(self, data, node):
        if not node:
            return False
        elif data == node.data:
            return True
        else:
            if data < node.data:
                return self._contains(data, node.left)
            else:
                return self._contains(data, node.right)

```

#### Traverse Forward and Backward
We will use yield in this part. First of all, you can think of yield as "return", which is intuitive. It is first a return, which returns a certain value in the program, after which the program will not run any further. See it as return and then see it as part of a generator (functions with yield are the real iterators).
yield from replaces for loops. The first thing the yield from x expression does with the x object is to call iter(x), getting the iterator from it. So x can be any iterable object.


```python
    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root

    def _traverse_forward(self, node):
        # Does a forward traversal (in-order traversal) through the BST.
        # yield will allow to print in this format 
        # for x in tree:
        #   print(x)
        if node:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
```
This is the function of traverse forward. We can see that we first yield from the left of the node, then yield the value of the node, and then yield from the right of the node. That is to say, the program will return the values in this tree from small to large

So what should we do when we want to traverse backward? Some students may have thought of it. If we want to read from big to small, then we first yield from the right, yield the value, and then yield from the left, right?

```python
  def __reversed__(self):
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        # Does a backward traversal (reverse in-order traversal) through the BST.
        # yield will allow to print in this format 
        # for x in tree:
        #   print(x)
        if node:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
```
In the above code, both __iter__ and __reversed__ are iterators to classes in python. When we write them into the code, we can iterate over the class in a for loop.
They allow us to iterate the class in this way.
```python
# Forward
for x in b_s_tree:
    print(x, end=" ")
print()
# Backward
for x in reversed(b_s_tree):
    print(x, end=" ")
print()
```

### Example
Now let's check your mastery with an example. We learned how to traverse forward and backward. Now we want to traverse in the order in which the tree was written and its reverse order, how should we implement it? That is to say, the data is read layer by layer from the root of the tree and read from the leaves up layer by layer.
Template: [postorder and preorder](tree_example.py)
Solution: [postorder and preorder](BST_post_pre_order.py)

### Problem
This problem is done recursively. Converts a BST to an array in ascending order.
Template: [to list](to_list.py)
Solution: [solution](to_list_solution.py)