class Solution:
    def sortSentence(self, s: str) -> str:
        txt=s[::-1].split(" ")
        txt.sort()
        array=[]
        for word in txt:
            array.append(word[1:][::-1])
        text=" ".join(array)
        return text
