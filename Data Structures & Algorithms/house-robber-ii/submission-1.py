class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        def solve(subset):
            memo = {}
            def dfs(i):
                # Base case: out of bounds
                if i >= len(subset):
                    return 0
                if i in memo:
                    return memo[i]
                
                # Forward logic: 
                # Take current + jump 2 OR skip current + move to next
                res = max(subset[i] + dfs(i + 2), dfs(i + 1))
                memo[i] = res
                return res
            
            return dfs(0)

        # Scenario A: House 0 to N-2 (ignore last)
        # Scenario B: House 1 to N-1 (ignore first)
        return max(solve(nums[:-1]), solve(nums[1:]))