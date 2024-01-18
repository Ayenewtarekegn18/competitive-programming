class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for i in nums:
            if i == 0:
                count+=1
            else:
                product *= i
        suffix = [product for _ in range(len(nums))]
        for j in range(len(suffix)):
            if nums[j] != 0 and count==0:
                suffix[j] //= nums[j]
            elif nums[j] !=0 and count == 1:
                suffix[j] *= 0
            elif count >1:
                suffix[j] *= 0
        return suffix
        