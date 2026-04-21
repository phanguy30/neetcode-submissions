class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # Rows (height) and Cols (width)
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            # 1. Boundary check MUST come first
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return
            
            # 2. Mark as visited (sink the land)
            grid[i][j] = "0"
            
            # 3. Explore neighbors
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        res = 0
        for i in range(rows):
            for j in range(cols):
                # Input is typically strings "1", not integer 1
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
                    
        return res