class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_store = defaultdict(set)
        column_store = defaultdict(set)
        square_store = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]== ".":
                    continue
                if board[i][j] not in row_store[i]:
                    row_store[i].add(board[i][j])
                else:
                    return False
                if board[i][j] not in column_store[j]:
                    column_store[j].add(board[i][j])
                else:
                    return False
                
                curr_square = (i//3)*3 + (j//3)
                
                if board[i][j] not in square_store[curr_square]:
                    square_store[curr_square].add(board[i][j])
                else:
                    return False
            
        return True



        