class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        i = len(s)-1
        j = i
        print(len(s))
        count = 0
        while i >= 0 :
            while j >= 0 and s[j] == '1':
                if i == j:
                    i-=1
                j-=1
            print(i,j)    
            if s[i] == '1':
                s[i],s[j] = s[j],s[i]
                count+= j-i
                j-=1
            i-=1
        return count
            