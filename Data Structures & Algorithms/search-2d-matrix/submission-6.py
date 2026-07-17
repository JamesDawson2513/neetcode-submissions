class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n*m - 1
        while l<=r:
            mid = (l+r) // 2
            print(l, mid, r)
            if matrix[mid // m][mid % m] < target:
                l = mid + 1
            elif matrix[mid // m][mid % m] > target:
                r = mid - 1
            else:
                return True
        return False
            
            
        