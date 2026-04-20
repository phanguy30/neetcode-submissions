class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        mem = {}

        def dfs(i):
            if i <= 1:
                return cost[i]
            if i in mem:
                return mem[i]
            
            mem[i] = cost[i]+ min(dfs(i-1), dfs(i-2))

            return mem[i]
        n = len(cost)
        
        return min(dfs(n - 1), dfs(n - 2))

            


        