class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = 1
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        n,m = len(str1), len(str2)
        for i in range(1,m+1):
            if n % i == 0 and m % i == 0:
                gcd = i

        gcdstr = str1[0:gcd]

        for i in range(n//gcd):
            if str1[(i*gcd):((i+1)*gcd)] != gcdstr:
                return ""

        for i in range((m//gcd)):
            if str2[(i*gcd):((i+1)*gcd)] != gcdstr:
                return ""
        return str1[0:gcd]


