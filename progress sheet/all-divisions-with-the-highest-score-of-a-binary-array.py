class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        division_sum = [left + right]
        for i in range(len(nums)):
            if nums[i] == 0:
                left += 1
            if nums[i] == 1:  
                right -= 1
            division_sum.append(left + right) 
        maxx = max(division_sum)
        result_indices = []
        for i, v in enumerate(division_sum):
            if v == maxx:
                result_indices.append(i)

        return result_indices



        