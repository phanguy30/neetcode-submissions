class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_path = []
        res = []
        n = len(nums)

        def dfs(i,remaining):
            if remaining < 0:
                return 
            if remaining == 0:
                res.append(curr_path[:])
                return
            
            
            for j in range(i,n):
                curr_path.append(nums[j])
                dfs(j, remaining - nums[j])
                curr_path.pop()
            
        dfs(0,target)

        return res
                

            
