class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m*n - 1
        while l <= r:
            mid = (l + r)//2
            mid1 = mid % m
            mid0 = mid//m
            print(mid, mid%m, mid - mid0%m)
            cur = matrix[mid0][mid1]
            if cur < target:
                l = mid + 1
            elif cur > target:
                r = mid - 1
            else:
                return True

        return False
