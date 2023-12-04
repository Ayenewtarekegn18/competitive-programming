class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        l=[""]
        i=0
        while i+2<len(num):
            if num[i]==num[i+1]==num[i+2]:
                ans+= num[i] + num[i+1] + num[i+2]
                l.append(ans)
                ans=""
                i+=1
            else:
                i+=1
        
        return max(l)