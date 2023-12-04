class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        extra = []
        ans = []
        maxn = 0
        for i in candies:
            extra.append( i + extraCandies )
            maxn = max(maxn,i)
        for j in extra:
            if j>=maxn:
                ans.append(True)
            else:
                ans.append(False)
        return ans