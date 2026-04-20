class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Quick length check: if total chars don't match, it's impossible
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(i, j):
            # Base case: if we consumed all characters of s1 and s2
            if i == len(s1) and j == len(s2):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = False
            
            # Option 1: Try taking a char from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    ans = True
            
            # Option 2: Try taking a char from s2 (only if Option 1 didn't already succeed)
            if not ans and j < len(s2) and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    ans = True
            
            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)