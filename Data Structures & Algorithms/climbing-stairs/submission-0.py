class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(remaining):
            # Base cases
            if remaining == 0: return 1  # Found 1 valid way to reach the top
            if remaining < 0: return 0   # Overshot the steps
            
            # Check memo
            if remaining in mem:
                return mem[remaining]
            
            # Recursive step: sum of taking 1 step and taking 2 steps
            mem[remaining] = dfs(remaining - 1) + dfs(remaining - 2)
            return mem[remaining]

        return dfs(n)