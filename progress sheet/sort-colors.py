class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b, c = 0, 0, 0

        for num in nums:
            if num == 0:
                a += 1
            elif num == 1:
                b += 1
            else:
                c += 1

        for i in range(len(nums)):
            if a != 0:
                a -= 1
                nums[i] = 0
            elif b != 0:
                b -= 1
                nums[i] = 1
            else:
                c -= 1
                nums[i] = 2