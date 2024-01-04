class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_point= sorted(points, key = lambda x:sqrt(x[0]**2 + x[1]**2))[:k]
        return closest_point