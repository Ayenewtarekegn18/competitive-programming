class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [point[0] for point in points]
        x.sort()   
        maxwidth = 0
      
        for i in range(1, len(x)):
            width = x[i] - x[i - 1]
            maxwidth = max(width,maxwidth)

        return maxwidth