class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                count+=1
            if count>1:
                return False
        return True
