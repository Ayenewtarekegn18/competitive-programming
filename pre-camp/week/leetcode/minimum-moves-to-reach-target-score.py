class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target>1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    target//= 2
                    maxDoubles -= 1
                    count += 1
                else:
                    target -=1
                    count  += 1
            else:
                count+= target-1
                break
        return count
