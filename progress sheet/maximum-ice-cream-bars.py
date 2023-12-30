class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        i=0
        while i < len(costs):
            if costs[i]>coins:
                 break
            coins-=costs[i]
            count=count+1
               
            i=i+1
        return count

