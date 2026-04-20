class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo, hi = sorted([p.val, q.val])

        if lo <= root.val <= hi:
            return root
        elif root.val < lo:
            return self.lowestCommonAncestor(root.right, p, q)
        else:  # root.val > hi
            return self.lowestCommonAncestor(root.left, p, q)