def max_depth(self, root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
        # Base case: if root is None, return the depth
        if not root:
            return depth
        
        # Calculate depth of left and right subtrees
        left_depth = dfs(root.left, depth + 1)
        right_depth = dfs(root.right, depth + 1)

        # Return the maximum depth among left and right subtrees
        return max(left_depth, right_depth)

    return dfs(root, 0)


# Examples:
# root = [3,9,20,null,null,15,7]  # 3
# root = [1,null,2]  # 2
# root = []  # 0
