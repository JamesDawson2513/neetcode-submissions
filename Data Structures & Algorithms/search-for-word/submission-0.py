class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:

            if k == len(word):
                return True

            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[k]):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)
            )

            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False