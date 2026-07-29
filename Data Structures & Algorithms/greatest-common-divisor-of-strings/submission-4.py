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
        return str1[0:gcd] if (str1 == gcdstr * (n//gcd) and str2 == gcdstr * (m//gcd)) else ""


