class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_path = []

        def dfs(i):
            if i == len(s):
                res.append(curr_path.copy())
            
            for j in range(i,len(s)):
                suffix = s[i:j+1]
                if is_palindrome(suffix):
                    curr_path.append(suffix)
                    dfs(j+1)
                    curr_path.pop()
        
        def is_palindrome(s):
            l,r = 0, len(s)-1
            while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False 
            return True
        dfs(0)
        return res


        