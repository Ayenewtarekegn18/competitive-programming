class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        b = set()
        maxvalue = 0
        i = 0
        j = 0
        val = 0
        while j < len(nums) and i < len(nums):
            if nums[j] in b:
                maxvalue = max(maxvalue,val)
                val -= nums[i]
                b.remove(nums[i])
                i+=1
            else:
                b.add(nums[j])
                val +=nums[j]
                j+=1       
        maxvalue = max(maxvalue,val)       
        return maxvalue
            
            
