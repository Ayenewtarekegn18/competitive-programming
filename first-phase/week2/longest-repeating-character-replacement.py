class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxim=0
        dic=defaultdict(int)
        for j in range(len(s)):
            dic[s[j]]+=1
            maxim = max(maxim,dic [ s [ j ] ] )
            if ( j - l + 1 ) > maxim + k:
                dic[ s [ l ] ] -= 1
                l += 1
        return len( s ) - l
        