# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(root):
            if not root:
                return []
            res = []
            q = deque([root])

            while q:
                n = len(q)
                level_nodes = []
                for _ in range(n):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level_nodes.append(node.val)
                res.append(level_nodes)
            return res
        
        levels = bfs(root)

        out = []

        for level in levels:
            out.append(level[-1])
        return out
            



        