class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        j=0
        num=0
        if len(nums)==1:
            if nums[0]==0:
                return 0
            else:
                return 1
        while j<len(nums) and i<len(nums):
            if nums[i]==0:
                i+=1
            elif nums[i]==1 and nums[j]==1:
                num=max(num,j-i+1)
                j+=1
            elif nums[j]==0:
                i=j
                j+=1
        return num
            
            