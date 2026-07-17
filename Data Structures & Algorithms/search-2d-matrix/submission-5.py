class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def finder(l,r):
            print('l: ', l, ', r: ', r)
            mid = (l + r) // 2
            mrow, mcol = (mid // n), (mid - n*(mid // n))
            if matrix[mrow][mcol] == target:
                return True
            elif l >= r:
                return False
            elif matrix[mrow][mcol] < target:
                return finder(mid+1,r) 
            else:
                return finder(l,mid-1)
        res = finder(0,m*n-1)
        return res
            
            
        