class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr_path = []
        counter = 0

        def dfs(node):
            nonlocal counter
            if not node:
                return

            curr_path.append(node.val)

            if node.val == max(curr_path):
                counter += 1

            dfs(node.left)
            dfs(node.right)

            curr_path.pop()

        dfs(root)
        return counter