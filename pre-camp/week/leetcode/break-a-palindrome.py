class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        a_count = palindrome.count("a")
        if len(palindrome) == 1:
            return ""
        n = len(palindrome)
        for i in range(n):
            print(s[i])
            if s[i] != "a" and n - a_count > 1:
                s[i] = "a"
                break
            elif i == n-1:
                    s[i] = "b"
        return "".join(s)
    
             
