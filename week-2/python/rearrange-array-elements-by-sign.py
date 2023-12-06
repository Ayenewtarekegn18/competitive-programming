class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort(key= lambda x: x<0)
        j = len(nums)//2
        ans = []
        for i in range(len(nums)//2):
            ans.append(nums[i])
            ans.append(nums[j])
            j+=1
        return ans