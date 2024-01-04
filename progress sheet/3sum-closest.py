class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestsum = float('inf')
        ans = 0
       
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while (j<k):
                add = nums[j] + nums[k] + nums[i]
                if abs(add - target) < closestsum:
                    closestsum = abs(add - target)
                    ans = add
                    print(add)
                if add < target: 
                    j += 1

                else:
                    k -=1
                   

        return ans