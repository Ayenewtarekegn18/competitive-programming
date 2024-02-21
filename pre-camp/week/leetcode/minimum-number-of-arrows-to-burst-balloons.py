class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        right = -inf
        print(points)
        for i in range(len(points)):
            if right  < points[i][0]:
                ans += 1
                right = points[i][1]
            else:
                right = min(points[i][1],right)
           
        
        return ans
