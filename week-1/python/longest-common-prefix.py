class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        f=strs[0]
        b=strs[-1]
        i=0
        ans=""
        length=min(len(f),len(b))
        while i<length:
            if (f[i]==b[i]):
                ans=ans+f[i]
            else:
                break
            i+=1
        return ans



