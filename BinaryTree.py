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
PLAN
- I am going to init a stack so we can keep track of our previous nodes
- we would traverse down the left subtree until there is no more nodes
- once we hit null we are going to backtrack and set that particular node to visited 
- then we would traverse down into the right subtree
- return the lst of nodes in order
TIME COMPLEXITY: O(N) SPACE COMPLEXITY: O(log n) + O(N)
'''

'''
UNDERSTAND
- Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree
EDGE CASES
- if we have a empty root: return 0
INPUT:
- a root of a binary tree
OUTPUT:
- the size of the binary tree
PLAN
- we would do a in-order traversal
- we would explore the left subtree mark that node visisted then explore the right subtree
- I would add all these nodes to a res lst from there we just would need to return the length of the res array
- we will using a stack as well to backtracking to previous nodes once we hit null
TIME COMPLEXITY: O(N) SPACE COMPLEXITY: O(log n) 
'''


def size(root) -> int:
    if not root:
        return 0

    stack = []
    cnt = 0

    curr_node = root
    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = stack.pop()
        cnt += 1
        curr_node = curr_node.right

    return cnt


'''
UNDERSTAND
- Given a (value) and the (root) of a tree
- write a function find() that returns True
- if there is a node with the given (value) in the tree
- Assume that the tree is balanced
INPUT
- the root of a tree and a value 
OUTPUT
- return a bool indicating if this value is in our tree
PLAN
- I am going to init a stack to keep track of the previous nodes
- I going to traverse the left subtree
- if the element that we pop from the stack is == val: return True
- we would set the curr_node to the element that we pop for the stack
- we move to the right subtree
- if not found we will just return False
TIME COMPLEXITY: O(N) SPACE COMPLEXITY: O(log n)
EDGE CASES
- we could have a empty root: return False
- our input value could be empty as well: return False
'''


def find(root, value) -> bool:
    if not root or not value:
        return False

    stack = []
    curr_node = root

    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = stack.pop()
        if curr_node.val == value:
            return True
        curr_node = curr_node.right
    return False


# Value = 5, return True
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
root.right = TreeNode(5)
print(find(root, 5))

# Value = 10, return False
root1 = TreeNode(6)
root1.left = TreeNode(4)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(9)
root1.right.left = TreeNode(7)
print(find(root1, 10))

#Value = None, return False
root2 = TreeNode(6)
root2.left = TreeNode(4)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(5)
root2.right = TreeNode(8)
root2.right.right = TreeNode(9)
root2.right.left = TreeNode(7)
print(find(root2, None))

# Root = None, return False
root3 = None
print(find(root3, 15))
