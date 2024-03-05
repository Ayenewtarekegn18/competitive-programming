class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        subset = []
        nums.sort()
        def backtrack(indx):
            if tuple(subset) not in ans:
                ans.add(tuple(subset[:]))
            for i in range(indx,len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return list(ans)