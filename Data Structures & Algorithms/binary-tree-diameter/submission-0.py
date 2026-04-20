class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0 # Height of an empty node is 0
            
            # 1. Get the height of the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # 2. Update the global max diameter 
            # (The path through the current node)
            res = max(res, left + right)

            # 3. Return the height of the current node to its parent
            # (The longest single path going down)
            return 1 + max(left, right)
        
        dfs(root)
        return res