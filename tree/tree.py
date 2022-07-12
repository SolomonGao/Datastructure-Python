# BST sample

class BST():
    
    class node():

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

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

# Test
# b_s_tree = BST()
# b_s_tree.insert(5)
# b_s_tree.insert(3)
# b_s_tree.insert(7)
# b_s_tree.insert(2)
# b_s_tree.insert(4)
# b_s_tree.insert(6)
# b_s_tree.insert(8)

# print(3 in b_s_tree)
# print(10 in b_s_tree)

# for x in b_s_tree:
#     print(x, end=" ")
# print()

# for x in reversed(b_s_tree):
#     print(x, end=" ")
# print()
