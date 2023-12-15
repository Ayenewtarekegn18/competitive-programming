class Bitset:

    def __init__(self, size: int):
        self.bit0 = ["0"]* size
        self.bit1 = ["1"]* size
        self.count1 = 0
        self.count0 = size
        self.size = size
        
    def fix(self, idx: int) -> None:
        if  self.bit0[idx] == "0" and self.count0 >= 1:
            self.bit0[idx] = "1"
            self.bit1[idx] = "0"
            self.count1 += 1
            self.count0 -= 1

    def unfix(self, idx: int) -> None:
        if  self.bit0[idx] == "1" and self.count1 >= 1:
            self.bit0[idx] = "0"
            self.bit1[idx] = "1"
            self.count1 -= 1
            self.count0 += 1

    def flip(self) -> None:
        self.bit0,self.bit1 = self.bit1,self.bit0
        self.count0, self.count1 = self.count1, self.count0
        
    def all(self) -> bool:
        return self.count1 == self.size

    def one(self) -> bool:
        return self.count1 >= 1
           
    def count(self) -> int:
        return self.count1 

    def toString(self) -> str:
        return "".join(self.bit0)

        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()