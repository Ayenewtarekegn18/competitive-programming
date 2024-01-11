class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = 0
        i = 0
        j = 1
        nums.sort(reverse = True)
        if len(nums) == 1:
            return 1
        while j < len(nums):
            while nums[i] - nums[j] > k:
                i+=1
                k += (nums[i-1] - nums[i])*(j-i)
            freq=max(freq,j-i+1)
            k -= (nums[i] - nums[j])
            j+=1
        return freq
        
