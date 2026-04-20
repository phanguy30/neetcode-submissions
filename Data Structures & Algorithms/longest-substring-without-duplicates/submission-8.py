class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        l,r = 0,1
        max_len = 1
        curr_str = s[0]
        while r < len(s):
            if s[r] not in curr_str:
                curr_str+=s[r]
                max_len = max(max_len, len(curr_str))
                r+=1
            else:
                
                l+=1
                curr_str = s[l:r]
            
        

        return max_len