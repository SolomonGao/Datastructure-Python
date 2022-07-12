from tree import BST

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(10)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(12)


res = []
def BST_to_list(root):
    if not root:
        return None
    if root.left:
        BST_to_list(root.left)
    res.append(root.data)
    if root.right:
        BST_to_list(root.right)
    
BST_to_list(tree.root)
print(res)

