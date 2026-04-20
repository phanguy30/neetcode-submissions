class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}

        def dfs(i,j):
            if i <0 or j<0 :
                return 0
            if i == 0 and j == 0:
                return 1  
            if (i, j) in mem:
                return mem[(i, j)]

            mem[(i,j)] = dfs(i,j-1)+ dfs(i-1,j)

            return mem[(i,j)]
        
        return dfs(m-1,n-1)
            



        