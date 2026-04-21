class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # FIX: Ensure rows and cols match the grid's structure
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        
        max_res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    max_res = max(max_res, dfs(r,c))
        return max_res
