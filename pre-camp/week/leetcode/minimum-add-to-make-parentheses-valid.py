class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        parenthesis = [] 
        for i in s:
            if i == "(":
                parenthesis.append(i)
            elif i == ")" and len(parenthesis) > 0 and parenthesis[-1] == "(":
                parenthesis.pop()
            elif i == ")" and len(parenthesis) == 0 or parenthesis[-1] == ")" :
                parenthesis.append(i)
            print(len(parenthesis))   
                
        return len(parenthesis)