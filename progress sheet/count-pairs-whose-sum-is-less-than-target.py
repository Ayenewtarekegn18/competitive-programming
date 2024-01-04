class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
    
        count = 0
        for i in range(len(nums)):
           for j in range(len(nums)):
               if nums[i] + nums[j] < target and i < j:
                   print(nums[i],nums[j])
                   count += 1
        return count

