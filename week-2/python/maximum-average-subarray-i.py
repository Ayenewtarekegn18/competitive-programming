class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        ave = sum(nums[:k])
        max_ave=ave/k
        while j <len(nums):
            ave -= nums[i]
            ave += nums[j]
            max_ave=max(max_ave,ave/k)
            j += 1    
            i += 1 

        return max_ave

        