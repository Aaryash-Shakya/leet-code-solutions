def max_depth(self, root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root, 0)

# Examples:
# root = [3,9,20,null,null,15,7]  # 3
# root = [1,null,2]  # 2
# root = []  # 0
