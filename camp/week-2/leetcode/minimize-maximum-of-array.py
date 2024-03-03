class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_num = nums[0]
        prefix = nums[0]

        for idx in range(1, len(nums)):
            cur = nums[idx]
            prefix += cur
            if cur > max_num:
                max_num = max(max_num, math.ceil(prefix/ (idx + 1)))


        return max_num