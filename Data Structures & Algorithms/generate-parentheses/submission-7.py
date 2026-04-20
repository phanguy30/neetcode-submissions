class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(open_used: int, close_used: int, curr: str):
            if open_used == n and close_used == n:
                res.append(curr)
                return

            if open_used < n:
                dfs(open_used + 1, close_used, curr + "(")

            if close_used < open_used:
                dfs(open_used, close_used + 1, curr + ")")

        dfs(0, 0, "")
        return res