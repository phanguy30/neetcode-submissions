# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(q,p):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            return (p.val == q.val) and (dfs(q.left,p.left)) and (dfs(q.right,p.right))
        return dfs(p,q)



            


            
        