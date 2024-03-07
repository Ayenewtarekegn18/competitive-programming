class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        pre = defaultdict(int)
        pre[0] = -1

        total = sum(nums) % p
        if not total :
            return 0

        pre_r = 0
        count = len(nums)
        for i in range(len(nums)):
            pre_r += nums[i]

            pre_l = pre_r % p
            check = (pre_r %p - total) % p

            if check in pre:
                count = min(count, i - pre[check])

            pre[pre_l] = i
        return count if count < len(nums) else -1