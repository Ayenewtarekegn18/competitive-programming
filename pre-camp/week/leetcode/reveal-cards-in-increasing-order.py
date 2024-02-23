class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        cards = deque()
        deck.sort(reverse = True)
        for i in range(len(deck)):
            if len(cards) == 0:
                cards.append(deck[i])
            else:
                x = cards.popleft()
                cards.append(x)
                cards.append(deck[i])
        return list(cards)[::-1]
            