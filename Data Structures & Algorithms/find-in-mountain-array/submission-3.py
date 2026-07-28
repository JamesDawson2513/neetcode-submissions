class Solution:

    def findAfter(self, target: int, arr: 'MountainArray',l: int, r: int) -> int:
        while l <= r:
            mid = (l+r) // 2
            cur = arr.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        l, r = 0, arr.length() - 1
        performed = False
        res = -1
        while l <= r:
            mid = (l+r)//2
            cur = arr.get(mid)
            if mid == arr.length() - 1 or cur < arr.get(mid + 1):
                if cur == target:
                    res = mid
                    break
                if cur < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if cur >= target and not performed: 
                    res = self.findAfter(target, arr, mid, r)
                    performed = True
                r = mid - 1
        return res