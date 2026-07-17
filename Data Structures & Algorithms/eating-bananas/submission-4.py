class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finder(l,r): 
            #l is the minimum number of bananas each hours to try meet the condition
            #r is the maximum number of bananas each hour to try meet the condition
            if l == r:
                return l 
            m = (l + r) // 2
            total = 0
            for pile in piles:
                #Calculating the hours to finish all piles given eating rate m
                total += (pile // m) + max(0, 1 if ((pile / m) - (pile // m)) > 0 else 0)
            if total <= h:
                return finder(l,m)
            else:
                return finder(m+1,r)
        Sum = 0
        Max = 0
        for s in piles:
            Sum += s
            Max = max(Max,s)
        r = Max
        l = max(Sum // h, 1)
        res = finder(l,r)
        return res