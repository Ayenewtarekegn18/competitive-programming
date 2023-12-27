class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        cumulative_sum = {num: sum(counts[key] for key in counts if key < num) for num in nums}
        ans = [cumulative_sum[num] for num in nums]
        return ans