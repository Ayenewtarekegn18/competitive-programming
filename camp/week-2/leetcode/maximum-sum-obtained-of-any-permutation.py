class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        temp=[0]*(len(nums)+1)
        for i in requests:
            temp[i[0]]+=1
            temp[i[1]+1]-=1
        for i in range(1,len(temp)):
            temp[i] += temp[i - 1]
        
        temp.pop()
        
        nums.sort()
        temp.sort()
        

        ans = 0
        for i in range(len(nums)):
            ans+=temp[i]*nums[i]

        return ans % (10**9 + 7)