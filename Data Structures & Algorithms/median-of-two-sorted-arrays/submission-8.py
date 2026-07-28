class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = [-float("inf")] + nums1 + [float("inf")]
        B = [-float("inf")] + nums2 + [float("inf")]

        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(A) - 1

        while l <= r:
            mid = (l + r) // 2
            r2 = half - mid

            if A[mid] <= B[r2 + 1] and B[r2] <= A[mid + 1]:
                max_left = max(A[mid], B[r2])
                min_right = min(A[mid + 1], B[r2 + 1])

                if total % 2 == 1:
                    return float(min_right)
                else:
                    return (max_left + min_right) / 2.0

            elif A[mid] > B[r2 + 1]:
                r = mid - 1
            else:
                l = mid + 1