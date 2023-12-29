class Solution:
    def sortSentence(self, s: str) -> str:
        result = ""
        p = [ word[-1] + word[:-1] for word in s.split()]
        
        p.sort()

        for word in p:
            result += word[1:] + ' '

        return result.rstrip()