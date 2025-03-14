class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#In-Order
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)
#Pre-Order - first visit
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
#Post Order - last visit
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

#REVERSE TRAVERSAL
#Reversed In-Order
def reverse_inorder_traversal(root):
    if root:
        reverse_inorder_traversal(root.right)
        print(root.value, end=" ")
        reverse_inorder_traversal(root.left)

#Reversed Pre-Order - first visit
def reverse_preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        reverse_preorder_traversal(root.right)
        reverse_preorder_traversal(root.left)
#Reversed Post Order - last visit
def reverse_postorder_traversal(root):
    if root:
        reverse_postorder_traversal(root.right)
        reverse_postorder_traversal(root.left)
        print(root.value, end=" ")

def swap_subtrees(root):
    if root:
        root.left, root.right = root.right, root.left
        swap_subtrees(root.left)
        swap_subtrees(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In-order Traversal")
inorder_traversal(root)
print("\nPre-order Traversal")
preorder_traversal(root)
print("\nPost order Traversal")
postorder_traversal(root)

print("\n\nSwapping Subtrees...")
swap_subtrees(root)

print("In-order Traversal After Swap")
inorder_traversal(root)
print("\nPre-order Traversal After Swap")
preorder_traversal(root)
print("\nPost order Traversal After Swap")
postorder_traversal(root)