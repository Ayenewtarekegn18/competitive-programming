class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l = 0
        r = max(max(houses),max(heaters)) - min(min(houses),min(heaters))
        ans = 0
        while l <= r:
            mid = (l+r)//2
            i = j = 0
            flag = True
            while i < len(houses) and j < len(heaters):
                if heaters[j] - mid <= houses[i] <= heaters[j] +mid:
                    i+=1
                else:
                    j+=1
                    
            if j >= len(heaters):
                flag = False
            
            if flag :
                ans = mid
                r = mid -1
            else:
                l = mid +1
        return ans

        