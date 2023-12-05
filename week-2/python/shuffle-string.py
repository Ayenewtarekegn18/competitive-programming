class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = []
        shuffle = ""
        for i in range(len(s)):
            shuffled.append("o")
        for j in range(len(s)):
            shuffled[int ( indices [j] ) ] = s[ j ]
        for k in shuffled :
            shuffle += k
        return shuffle