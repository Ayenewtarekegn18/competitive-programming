class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [ 0 for _ in range(len(s)+1)]
        for i in shifts :
            if i[2] == 1:
                prefix[i[0]] +=1
                prefix[i[1]+1] -=1
            else:
                prefix[i[0]] -=1
                prefix[i[1]+1] +=1
        total = 0
        for j in range(len(prefix)):
            total +=prefix[j]
            prefix[j] = total
        ans= ""
        for k in range(len(s)):
            ans+= chr((ord(s[k]) + prefix[k] - 97 ) % 26 + 97)
        return ans
            

