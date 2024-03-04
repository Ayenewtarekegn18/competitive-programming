class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def backtrack(indx):
            ans.append(subset.copy())
            for i in range(indx,len(nums)):
                subset.append(nums[i])
                backtrack( i + 1 )
                subset.pop()
        backtrack(0)
        return ans
    