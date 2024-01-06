class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        count = 0
        ans = 0

        for i in range(n):
            if nums[i] == 0:
                count += 1

            while count > k:
                if nums[j] == 0:
                    count -= 1
                j += 1

            ans = max(ans, i - j + 1)

        return ans