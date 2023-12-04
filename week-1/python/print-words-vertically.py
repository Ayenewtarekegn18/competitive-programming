class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        max_len = max([len(word) for word in s])
        ans = [""] * max_len
        for i in range(len(s)):
            if len(s[i]) < max_len:
                s[i] += " " * (max_len - len(s[i]))
        for i in range(len(s)):
            for j in range(len(s[i])):
                ans[j] += s[i][j]
        for i in range(max_len):
            ans[i] = ans[i].rstrip()

        return ans
