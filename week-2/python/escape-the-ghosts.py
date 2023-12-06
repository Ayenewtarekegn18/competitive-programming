class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghost = 100000000
        for i in ghosts:
           ghost = min( ghost, abs(target[0]-i[0]) + abs(target[1]-i[1]))
        if ghost> abs(target[0]- 0) + abs(target[1]-0):
            return True
        else:
            return False

        