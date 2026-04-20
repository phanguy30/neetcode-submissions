class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # Odd length palindromes (e.g., "aba")
            count += self.expand(s, i, i)
            # Even length palindromes (e.g., "aa")
            count += self.expand(s, i, i + 1)
            
        return count

    def expand(self, s, l, r):
        current_count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current_count += 1
            l -= 1
            r += 1
        return current_count