class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        n = len(newStr)
        half = n//2
        for i in range(half):
            if newStr[i] == newStr[n-1-i]:
                continue
            else: 
                return False
        return True
        