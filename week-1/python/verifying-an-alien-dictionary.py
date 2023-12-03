class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        temp = {char: i for i, char in enumerate(order)}
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]) and j < len(words[i + 1]):
                if temp[words[i][j]] < temp[words[i + 1][j]]:
                    break
                if temp[words[i][j]] > temp[words[i + 1][j]]:
                    return False
                j += 1

            if j == len(words[i + 1]) and j < len(words[i]):
                return False

        return True