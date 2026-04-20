class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in mem:
                return mem[i]
            
            mem[i] = max(dfs(i-1), dfs(i-2)+ nums[i])

            return mem[i]

        return dfs(len(nums)-1)
        