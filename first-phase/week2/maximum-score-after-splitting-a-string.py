class Solution:
    def maxScore(self, s: str) -> int:
        total=0
        ans = 0
        pre =0
        prefix = []
        for i in s:
            total += int(i)
        for i in range(len(s)):
            pre += int(s[i])
            prefix.append(pre)
        
        for i,num in enumerate(prefix):
            if i == len(prefix)-1 and prefix[i] == prefix[i-1]:
                continue
            ans = max(ans,total - num + (i+1-num))
        
        return ans