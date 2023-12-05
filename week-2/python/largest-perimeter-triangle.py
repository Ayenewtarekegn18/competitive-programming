class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1
        while i-2 >= 0 :
            if nums[i] + nums[i-1] > nums[i-2] and nums[i-1] + nums[i-2] > nums[i] and nums[i] + nums[i-2] > nums[i-1]:
                return nums[i] + nums[i-1] + nums[i-2]
            else:
                i-=1
        else:
            return 0