class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles) - 1
        total_sum = 0

        while i < len(piles) // 3:
            total_sum += piles[j - 1]
            j -= 2
            i += 1

        return total_sum