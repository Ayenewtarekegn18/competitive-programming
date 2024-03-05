class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        l = 0
        r = len(cardPoints) - k

        sub_sum = sum(cardPoints[r:])
        ans = sub_sum

        while r < len(cardPoints):
            sub_sum += (cardPoints[l] - cardPoints[r])
            ans = max(ans,sub_sum)
            l += 1
            r += 1

       
        return ans
