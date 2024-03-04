class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        min_unf = float("inf")
        if len(cookies) == k:
          
            return max(cookies)
        def backtrack (i):
            nonlocal min_unf
            if i == len(cookies):
                unf = max(children)
                min_unf = min(min_unf,unf)
                return
            for j in range(k):
                children[j] += cookies[i]
                backtrack(i+1)
                children[j] -= cookies[i]
        backtrack(0)
        return min_unf
