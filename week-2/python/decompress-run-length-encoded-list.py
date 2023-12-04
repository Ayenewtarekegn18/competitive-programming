class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            if i%2==1:
                continue
            else:
                while nums[i] > 0:
                    ans.append(nums[i+1])
                    nums[i] -= 1
        return ans
            




