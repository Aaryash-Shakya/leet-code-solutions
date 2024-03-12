# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def preorder_traversal(root):
    traversal = []
    def explore_node(node):
        if node is None:
            return
        else:
            traversal.append(node.val)
            explore_node(node.left)
            explore_node(node.right)

    explore_node(root)    
    return traversal