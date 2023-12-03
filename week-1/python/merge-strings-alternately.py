class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        ans=""
        for _ in range(max(len(word1),len(word2))):
            if (i<len(word1)):
                ans+=word1[i]
            if j<len(word2):
                ans+=word2[j]
            i+=1
            j+=1
        return ans
