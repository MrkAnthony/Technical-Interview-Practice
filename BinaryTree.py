from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list
    if not root:
        return []
    # Create an empty queue using deque
    # Create an empty list to store the explored nodes
    queue = deque([root])
    result = []

    # Add the root to the queue
    # While the queue is not empty:
    while queue:
        node_popped = queue.popleft()
        #print(node_popped)
        # Pop the next node off the queue (pop from the left side!)
        # Add the popped node to the list of explored nodes
        result.append(root.val)

        # Add each of the popped node's children to the end of the queue
        queue.append(node_popped)
    # Return the list of visited nodes
    return result

#root = TreeNode(4, TreeNode(2, TreeNode(1,TreeNode(6)), TreeNode(3))) # Expected [4, 2, 6, 1, 3]
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
print(level_order(root))
