class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        zero_row = [0] * (cols + 2)
        padded = [zero_row] + [[0] + row + [0] for row in grid] + [zero_row]
        for row in padded:
            print(row)
        for i in range(rows + 1):
            for j in range(cols + 1):
                if padded[i][j] != padded[i+1][j]:
                    res += 1
                if padded[i][j] != padded[i][j+1]:
                    res += 1
                print(res)
        return res



