class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = 0
        max_length_T = 0
        max_length_F = 0
        n = 0
    # checking for the maximum interval for True
        for j in range(len(answerKey)):
            if answerKey[j] == "F":
                n += 1
            while n > k:
                if answerKey[i] == "F":
                    n -= 1
                i += 1
            max_length_T = max(max_length_T, j - i+1)
        
        i = 0
        n = 0
# checking for the maximum interval for False
        for t in range(len(answerKey)):
            if answerKey[t] == "T":
                n += 1
            while n > k:
                if answerKey[i] == "T":
                    n -= 1
                i += 1
            max_length_T = max(max_length_T, t - i+1)

        return max(max_length_T,max_length_F)