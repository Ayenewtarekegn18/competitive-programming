class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = 0
        prefix = []
        for i in nums:
            total += i
            prefix.append(total)
        j = len(prefix)-1
        minindex = float("inf")
        flag = True
        while j >= 0:
            if j > 0 and (prefix[-1]-prefix[j]) == (prefix[j-1]):
                minindex = min(minindex,j)
                flag = False
            elif j == 0 and (prefix[-1]-prefix[j]) == 0:
                minindex = min(minindex,j)
                flag = False
            j-=1
        if flag:
            return -1
        else:
            return minindex