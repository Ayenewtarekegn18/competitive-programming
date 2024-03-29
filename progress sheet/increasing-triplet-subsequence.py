class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x= nums[0]
        y= float('inf')

        count = 0
        for n in nums:
            if x >= n:
                x = n
            elif y >= n:
                y = n
            else:
                return True

        return False
        