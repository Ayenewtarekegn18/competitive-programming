class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        maps = set(nums)
        for i in range(len(nums)+1):
            if i not in maps:
                return i

