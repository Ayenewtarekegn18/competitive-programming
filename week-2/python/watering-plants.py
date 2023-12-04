class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        temp=capacity
        for i in range(len(plants)):
            if plants[i]>temp:
                temp=capacity
                temp-=plants[i]
                ans+=i+i+1
            else: 
                ans+=1
                temp-=plants[i]
        return ans