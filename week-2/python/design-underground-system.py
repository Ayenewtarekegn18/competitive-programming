class UndergroundSystem:

    def __init__(self):
        self.map={}
        self.res=defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.map[id]=[stationName,t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.res[(self.map[id][0],stationName)].append(t-self.map[id][1])     
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        l=len(self.res[(startStation,endStation)])
        s=sum(self.res[(startStation,endStation)])
        return s/l
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)