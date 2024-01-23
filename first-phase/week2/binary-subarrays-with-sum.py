class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pri=defaultdict(int)
        pri[0]=1
        count=0
        running_sum=0
        for i in nums:
            running_sum+=i
            if running_sum-goal in pri:
                count+=pri[running_sum-goal]
            pri[running_sum]+=1
        return count