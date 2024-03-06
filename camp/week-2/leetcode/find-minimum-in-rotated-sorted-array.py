class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minim = float("inf")
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= nums[r]:
                r = mid -1
                minim = min(minim,nums[mid])
            else:
                l = mid + 1
        return minim


