class TimeMap:

    def __init__(self):
        self.di = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.di[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.di:
            l = 0 
            r = len(self.di[key]) -1
            ans=''
            while l <=r:
                mid = (l+r)//2
                if self.di[key][mid][1] <= timestamp:
                    ans = self.di[key][mid][0]
                    l = mid +1
                else:
                    r = mid - 1
            
            return ans
        return "" 

                     


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)