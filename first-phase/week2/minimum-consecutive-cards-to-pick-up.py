class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        index = {}
        minimum = float("inf")
        flag = True
        for i in range(len(cards)):
            if cards[i] in index:
                minimum = min (minimum,i-index[cards[i]]+1)
                index[cards[i]] = i
                flag = False
            else:
                index[cards[i]] = i
        
        if flag :
            return -1
        else:
            return minimum