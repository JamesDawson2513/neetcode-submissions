class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lower = set()
        upper = set()
        sequences = {}
        res = 0

        for num in nums:
            if num in sequences:
                continue

            Bool = False
            Bool2 = False

            if num in lower:
                Bool = True
                Bool2 = True
                sequences[num] = sequences[num + 1]
                sequences[sequences[num]] = num
                lower.remove(num)
                if num not in upper:
                    lower.add(num - 1)

            if num in upper:
                if not Bool2:
                    sequences[num] = num
                Bool = True
                sequences[sequences[num]] = sequences[num - 1]
                sequences[sequences[num - 1]] = sequences[num]
                upper.remove(num)
                upper.add(sequences[num] + 1)

            if not Bool:
                sequences[num] = num
                lower.add(num - 1)
                upper.add(num + 1)

            left = num
            if num - 1 in sequences:
                left = sequences[num - 1]
            right = num
            if num + 1 in sequences:
                right = sequences[num + 1]
            
            sequences[left] = right
            sequences[right] = left
            lower.discard(num - 1)
            upper.discard(num + 1)

        for key, value in sequences.items():
            if key <= value:
                res = max(res, value - key + 1)

        return res
        