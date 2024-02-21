class MinStack:
    def __init__(self):
        self.ms = []
        self.as_ = []

    def push(self, val):
        if not self.as_:
            self.as_.append(val)
        else:
            self.as_.append(min(val, self.as_[-1]))
        self.ms.append(val)

    def pop(self):
        self.ms.pop()
        self.as_.pop()

    def top(self):
        return self.ms[-1]

    def getMin(self):
        return self.as_[-1] if self.as_ else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()