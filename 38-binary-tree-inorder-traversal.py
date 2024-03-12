# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def postorder_traversal(root):
    path = []
    def explore_node(node):
        if node is None:
            return
        else:
            explore_node(node.left)
            path.append(node.val)
            explore_node(node.right)

    explore_node(root)    
    return path