class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (p.val == q.val) and same_tree(p.left, q.left) and same_tree(p.right, q.right)

        if not subRoot:
            return True  # empty tree is subtree of any tree

        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val and same_tree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)