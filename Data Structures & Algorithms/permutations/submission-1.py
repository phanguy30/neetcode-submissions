class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_path= []
        
        def dfs(curr_path, remaining):
            # Base Case: If no numbers left to pick, we found a permutation
            if len(remaining) == 0:
                res.append(curr_path[:]) # Append a copy of the path
                return
            
            for i in range(len(remaining)):
                # Choose: Add current number to path
                curr_path.append(remaining[i])
                
                # Explore: Create a new list excluding the current element
                new_remaining = remaining[:i] + remaining[i+1:]
                dfs(curr_path, new_remaining)
                
                # Unchoose (Backtrack): Remove the number to try the next one
                curr_path.pop()
            
        dfs([], nums)
        return res