class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1 
        r = max(nums)
        while l <=r:
            mid = (l+r)//2
            ans = 0
            for i in nums:
                ans += ceil(i/mid)
            if ans <= threshold:
                r = mid -1
            else:
                l = mid + 1
        return l