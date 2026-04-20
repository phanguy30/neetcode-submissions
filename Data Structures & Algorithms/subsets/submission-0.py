class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_path = []
        res = []
        n = len(nums)
        
        def dfs(i):
            if i == n:
                res.append(curr_path[:])
                return
            
            # 1. Exclude nums[i]
            dfs(i + 1)
            
            # 2. Include nums[i]
            curr_path.append(nums[i])
            dfs(i + 1)
            
            # 3. Clean up (Backtrack)
            curr_path.pop()
        
        # MUST start at 0 to process the first element
        dfs(0) 

        return res