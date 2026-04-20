class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle the edge case of an empty input string
        if not digits:
            return []

        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        curr_path = []
        
        def dfs(i):
            # Base Case: We have picked one letter for every digit
            if i == len(digits):
                res.append("".join(curr_path))
                return 

            # Recursive Step: Try every letter mapped to the current digit
            for letter in digit_map[digits[i]]:
                curr_path.append(letter) # Make a choice
                dfs(i + 1)               # Explore
                curr_path.pop()          # Backtrack (undo the choice)
        
        dfs(0)
        return res