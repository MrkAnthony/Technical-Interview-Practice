from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def check_tree(root):
    if not root:
        return False

    res = 0
    if root.left and root.right:
        res += (root.left.val + root.right.val)
    elif root.left and not root.right:
        res += root.left.val
    elif root.right and not root.left:
        res += root.right.val
    return res == root.val


def left_most(root):
    if not root:
        return 0
    if not root.left:
        return 0

    deepest_node = 0
    while root.left:
        deepest_node = root.left.val
        root.left = root.left.left

    return deepest_node


'''
UNDERSTAND
- Given the root of a binary tree, return a list representing the inorder traversal of it's nodes values.
- In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.
INPUT: is the root of a binary tree
OUTPUT: a lst of nodes that show the traversal of inorder traversal
'''


def inorder_traversal(root) -> list[int]:
    pass


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(17)

print(inorder_traversal(root))