class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        freq = defaultdict(int)
        senate = list(senate)
        R = []
        D = []
        for i in senate:
            freq[i] += 1
        j = 0
        while freq["R"] > 0 and freq["D"] > 0:
            if senate[j] == "R":
                if len(R) > 0:
                    senate[j] = "N"
                    R.pop()
                else:
                    freq["D"] -=1
                    D.append("N")
            elif senate[j] == "D":
                if len(D) > 0:
                    senate[j] = "N"
                    D.pop()
                else:
                    freq["R"] -=1
                    R.append("N") 
            j+=1
            if j == len(senate):
                j = 0
        return "Radiant" if freq["D"] <= 0 else "Dire"