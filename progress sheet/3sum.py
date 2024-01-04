class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
       
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]: 
               continue
            j = i+1
            k = len(nums)-1
            while (j<k):
                if nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                else:
                    ans.add((nums[i],nums[j],nums[k]))
                    j +=1
                    k -=1
             
        return list(ans)
#  
#                 # -4 -1 -1 0 1 2
               
