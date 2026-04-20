class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            # Base case: We are at the start, 0 jumps needed
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            
            res = float('inf')
            
            # Look backwards: check every index 'j' that could reach 'i'
            # A jump from j can reach i if j + nums[j] >= i
            for j in range(i):
                if j + nums[j] >= i:
                    res = min(res, 1 + dfs(j))
            
            memo[i] = res
            return res

        return dfs(n - 1)