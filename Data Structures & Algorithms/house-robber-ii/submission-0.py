class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        # We run the helper on two scenarios:
        # 1. All houses except the last one
        # 2. All houses except the first one
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    
    def helper(self, houses):
        mem = {}

        def dfs(i):
            if i == 0: return houses[0]
            if i == 1: return max(houses[0], houses[1])
            
            if i in mem:
                return mem[i]
            
            # Use dfs(i-1) and dfs(i-2) so the recursion actually happens!
            mem[i] = max(dfs(i - 1), dfs(i - 2) + houses[i])
            return mem[i]

        return dfs(len(houses) - 1)