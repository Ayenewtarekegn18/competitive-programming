class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l =max(weights)
        r =sum(weights)
        minim = float("inf")
        while l <= r:
            mid = (l+r)//2
            val = 1
            capa = mid
            for weight in weights:
                if capa - weight < 0:
                    val+=1
                    capa=mid
                capa -= weight
            if val <= days:
                minim = min(minim,mid)
                r = mid-1
            else:
                l = mid + 1
        return minim
            


