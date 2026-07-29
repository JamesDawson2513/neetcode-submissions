class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l,r = 0,k-1

        while r < len(arr) - 1 :
            if x - arr[l] <= arr[r+1] - x:
                return arr[l:r+1]
            else:
                l += 1
                r += 1
        
        return arr[l:r+1]