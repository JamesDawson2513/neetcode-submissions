from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to track occurrences in rows, columns, and squares
        hashm = {
            "rows": {i: {} for i in range(1, 10)},
            "cols": {i: {} for i in range(1, 10)},
            "squares": {i: {} for i in range(1, 10)}
        }

        # Traverse each cell in the board
        for n in range(1, 10):
            for m in range(1, 10):
                cell_value = board[n-1][m-1]

                if cell_value == ".":
                    continue

                num = int(cell_value)

                # Check the row
                if hashm["rows"][n].get(num, False):
                    return False
                hashm["rows"][n][num] = True

                # Check the column
                if hashm["cols"][m].get(num, False):
                    return False
                hashm["cols"][m][num] = True

                # Calculate square index and check the square
                square_index = (3 * ((n - 1) // 3)) + ((m - 1) // 3) + 1
                if hashm["squares"][square_index].get(num, False):
                    return False
                hashm["squares"][square_index][num] = True

        return True



        
                
                    
                


        