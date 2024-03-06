class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        ans = 0 
        while r>= l:
            mid = (l + r)//2
            if mid*mid <=x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans