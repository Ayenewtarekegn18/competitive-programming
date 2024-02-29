class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1 for _ in range(k)]
        self.left = self.right = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False
        elif self.right == self.k-1:
            self.right = 0
            self.queue[self.right] = value
            self.count += 1
            return True
        elif self.right == -1:
            self.right += 1
            self.left += 1
            self.queue[self.right] = value
            self.count += 1
            return True
        else:
            self.right += 1
            self.queue[self.right] = value
            self.count += 1
            return True
        
    def deQueue(self) -> bool:
        if self.count == 0:
           return False
        elif self.left == self.k-1:
            self.count-=1
            self.left = 0
            return True
        else:
            self.count -= 1
            self.left += 1
            return True

    def Front(self) -> int:
        print(self.left,self.queue)
        if self.count == 0:
            return -1
        else:
            return self.queue[self.left]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        else:
            return self.queue[self.right]

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == self.k else False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()