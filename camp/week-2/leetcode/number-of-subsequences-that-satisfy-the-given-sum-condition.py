class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            l = i
            r = len(nums) - 1
            while l <= r:
                mid = (l + r )// 2
                if nums[mid] + nums[i] <=target:
                    l = mid+1
                else:
                    r = mid - 1
            if l - i:
                ans += 2**(l-i-1)
        return ans % (10**9 + 7) 
    
      
