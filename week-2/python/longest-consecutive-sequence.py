class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        count = 1
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] +1 == nums[i+1]:
                count += 1
                print(count)
            else:
                count = 1
            ans = max(ans,count)
        return ans
