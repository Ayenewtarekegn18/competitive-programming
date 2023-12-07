class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        ans = ""
        for j in range(len(s)):
            if i<len(spaces) and j==spaces[i]:
                ans+=" "
                i+=1
            ans +=s[j] 
        return ans