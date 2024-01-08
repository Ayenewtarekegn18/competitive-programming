class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        max_length = 0
        k = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                k += 1
            while k > 1:
                if nums[i] == 0:
                    k -= 1
                i += 1
            max_length = max(max_length, j - i)

        return max_length  

                 
        