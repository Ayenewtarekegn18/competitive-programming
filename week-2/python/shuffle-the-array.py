class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j=n
        i=0
        ans = []
        while j <len(nums):
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j+=1
        return ans
# 2 5 1 3 4 7
# 2 3 1 5 4 7
# 2 