class Solution:
    def num(self, n):
        x = 0
        while n != 0:
            temp = n % 10
            x += temp * temp
            n = n // 10
        return x
        
    def isHappy(self, n: int) -> bool:
        nums_set = set()
        while n != 1 and n not in nums_set:
            nums_set.add(n)
            n = self.num(n)
        return n == 1