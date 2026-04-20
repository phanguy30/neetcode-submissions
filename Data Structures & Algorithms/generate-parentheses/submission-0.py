class Solution:
    def generateParenthesis(self, n: int):
        res = []
        curr = []

        def dfs(open_used: int, close_used: int):
            if open_used == n and close_used == n:
                res.append("".join(curr))
                return

            # can add '(' if we still have opens left
            if open_used < n:
                curr.append("(")
                dfs(open_used + 1, close_used)
                curr.pop()

            # can add ')' only if it won't break validity
            if close_used < open_used:
                curr.append(")")
                dfs(open_used, close_used + 1)
                curr.pop()

        dfs(0, 0)
        return res
                    
                

