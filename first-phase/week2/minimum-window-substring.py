class Solution:
    def minWindow(self, s: str, t: str) -> str:
        di = defaultdict(int)
        t = Counter(t)
        l = 0
        ans = float("inf")
        result = ""
        i = 0
        j = 0
        for r in range(len(s)):
            if s[r] in t:
                di[s[r]] += 1
            while l < len(s) and all(di[c] >= t[c] for c in t):
                if ans > r - l + 1:
                    ans = r - l + 1
                    i = l
                    j = r + 1
                if s[l] in di:
                    di[s[l]] -= 1
                l += 1
        return s[i:j]
            
                    