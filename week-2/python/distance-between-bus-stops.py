class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        num=abs(destination-start)
        total=sum(distance)
        mn=min(start,destination)
        mx=max(start,destination)
        sm= sum(distance[mn:mx])
        return(min(sm,total-sm))

        