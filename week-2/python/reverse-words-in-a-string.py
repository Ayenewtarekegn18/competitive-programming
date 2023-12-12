class Solution:
    def reverseWords(self, s: str) -> str:
        n= s.split()[::-1]
        return " ".join(n)