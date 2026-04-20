class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l_row = 0

        h_row = m-1
        # Step 1: Find the correct row
        target_row = -1
        while l_row <= h_row:
            m_row = (l_row + h_row) // 2
            
            # Check if target is in the range of this row
            if target < matrix[m_row][0]:
                h_row = m_row - 1
            elif target > matrix[m_row][-1]:
                l_row = m_row + 1
            else:
                # Target is within this row's range
                target_row = m_row
                break
        
        # If no row was found, the target isn't in the matrix
        if target_row == -1:
            return False
        
        l_col = 0
        h_col = n-1

        # Step 2: Binary search within the identified row
        l_col, h_col = 0, n - 1
        while l_col <= h_col:
            m_col = (l_col + h_col) // 2
            if matrix[target_row][m_col] == target:
                return True
            elif matrix[target_row][m_col] < target:
                l_col = m_col + 1
            else:
                h_col = m_col - 1
                
        return False
            

                
        