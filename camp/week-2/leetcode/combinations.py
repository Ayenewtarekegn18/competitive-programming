class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def combination(first,path):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(first,n+1):
                path.append(i)
                combination(i + 1, path)
                path.pop()
        combination(1,[])
        return ans
            