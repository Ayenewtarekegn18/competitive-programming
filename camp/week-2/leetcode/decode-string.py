class Solution:
    def __init__ (self)->None:
        self.pos = 0

    def decodeString(self, s: str) -> str:
        ans = ""
        size = len(s)

        while self.pos < size:
            k = 0
            substr = ""
            if s[self.pos] == "]":
                self.pos +=1
                return ans
            
            while self.pos < size and  "0" <= s[self.pos] <= "9":
                k = k*10 + int(s[self.pos]) + int("0")
                self.pos+=1
            
            if s[self.pos] == "[":
                self.pos +=1
                substr = self.decodeString(s)
            while k > 0:
                ans += substr
                k-=1
            while self.pos < size and "a" <= s[self.pos] <= "z":
                ans += s[self.pos]
                self.pos+=1
        return ans

        