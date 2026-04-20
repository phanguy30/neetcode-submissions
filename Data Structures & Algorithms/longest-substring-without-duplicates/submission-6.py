class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        l = 0
        curr_str = set()
        res = 0

        for r in range(0, len(s)):
            while s[r] in curr_str:
                curr_str.remove(s[l])
                l+=1
            curr_str.add(s[r])
            res = max(res, r-l+1)

        
        return res


        