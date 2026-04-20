class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = set() # Track coordinates we've already used

        def dfs(i, j, curr):
            # 1. Success condition
            if curr == word:
                return True
            
            # 2. Boundary and Failure conditions
            if (i < 0 or j < 0 or i >= n or j >= m or 
                (i, j) in visited or 
                not word.startswith(curr)):
                return False
            
            # 3. Add current cell to path
            # We check if the NEW character matches the word's next character
            if board[i][j] != word[len(curr)]:
                return False
                
            visited.add((i, j))
            new_string = curr + board[i][j]

            # 4. Explore (must return True if ANY direction works)
            res = (dfs(i+1, j, new_string) or
                   dfs(i-1, j, new_string) or
                   dfs(i, j-1, new_string) or
                   dfs(i, j+1, new_string))
            
            # 5. Backtrack: remove from visited so other paths can use it
            visited.remove((i, j))
            
            return res

        for i in range(n):
            for j in range(m):
                # Start DFS from every cell
                if dfs(i, j, ""):
                    return True
        
        return False