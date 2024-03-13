# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def inorder_traversal(root):
    path = []

    def explore_node(node):
        # base case
        if node is None:
            return

        else:
            # explore left subtree
            explore_node(node.left)
            # add current node's value
            path.append(node.val)
            # explore right subtree
            explore_node(node.right)

    explore_node(root)
    return path


# Examples:
# root = TreeNode(1, None, TreeNode(2, TreeNode(3), None)) = [1, None, 2, 3]  # [1, 3, 2]
# root = TreeNode(1, TreeNode(2), TreeNode(3)) = [1, 2, 3]  # [2, 1, 3]
# root = TreeNode(1) = [1]  # [1]
