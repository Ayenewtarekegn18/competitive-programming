class Robot:

    def __init__(self, width: int, height: int):
        
        self.x = 0
        self.y = 0
        self.w = width
        self.h = height
        self.d = 0
        self.dir = [[1,0],[0,1],[-1,0],[0,-1]]
        self.dlab = ['East','North','West','South']

    def step(self, num: int) -> None:
        num %= 2*(self.w+self.h)-4
        if num == 0:
            num = 2*(self.w-1+self.h-1)
        for _ in range(num):
            nx, ny = self.x + self.dir[self.d][0], self.y + self.dir[self.d][1]
            while not (0<=nx<self.w and 0<=ny<self.h):
                self.d = (self.d+1)%4
                nx, ny = self.x + self.dir[self.d][0], self.y + self.dir[self.d][1]
            
            self.x = nx
            self.y = ny 

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        

    def getDir(self) -> str:
        return self.dlab[self.d]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()