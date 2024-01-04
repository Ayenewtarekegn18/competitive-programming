class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookies = sum(s)
        i = 0
        j = 0
        num = 0
        while(i < len(g) and j < len(s)):
            if g[i] > s[j]:
                j += 1  
            else:
                num +=1
                i+=1
                j+=1
        return num

