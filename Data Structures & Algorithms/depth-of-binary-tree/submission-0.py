class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_h = 0
        counter = 0

        def dfs(node):
            nonlocal max_h, counter # Allows us to modify variables outside this function
            if not node:
                return
            
            counter += 1
            max_h = max(max_h, counter)
            
            dfs(node.left)
            dfs(node.right)
            
            counter -= 1 # Backtrack: remove this node from the current path height

        dfs(root)
        return max_h