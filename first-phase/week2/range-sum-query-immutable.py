class NumArray:

    def __init__(self, nums: List[int]):
        self.NumArray = nums
        self.prefix = []
        total = 0
        self.prefix.append(total)
        for i in nums:
            total += i
            self.prefix.append(total)
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# 0 , 