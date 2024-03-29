class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        pair = [-1,-1]
        while l <=  r:
            mid = (l + r)//2
            if nums[mid] >= target:
                r = mid -1
                if nums[mid] == target:
                    pair[0] = mid
            elif nums[mid] < target:
                l = mid +1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] <= target:
                l = mid +1
                if nums[mid] == target:
                    pair[1]  = mid
            elif nums[mid] > target:
                r = mid-1
      
        return pair
        
        