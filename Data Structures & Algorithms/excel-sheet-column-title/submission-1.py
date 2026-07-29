class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = str()
        start = ord('A')
        while columnNumber > 0:
            columnNumber -= 1
            toadd = columnNumber % 26
            res += chr(start + toadd)
            columnNumber = columnNumber // 26
        return res[::-1]
