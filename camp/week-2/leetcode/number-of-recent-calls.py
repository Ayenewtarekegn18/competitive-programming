class RecentCounter:

    def __init__(self):
        self.stack = []
    def ping(self, t: int) -> int:
        self.stack.append(t)
        count  = 0
        for i in self.stack:
            if t-3000 <= i <= t:
                count+=1
        
        return count

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)