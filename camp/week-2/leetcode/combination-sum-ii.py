class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target > sum(candidates):
            return []
        candidates.sort()
        ans = set()
        def backtrack(indx,path):
            last_pop = float("inf")
            if sum(path) == target:
                if tuple(path) not in ans:
                    ans.add(tuple(path[:]))
                return 
            elif sum(path) > target:
                return
            for i in range(indx,len(candidates)):
                if last_pop == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1,path)
                last_pop = path.pop()
        backtrack(0,[])
        return list(ans)