class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mps = {}
        zeroloss = []
        oneloss = []
        for i in range(len(matches)):
            if matches[i][0] not in mps:
                mps[matches[i][0]]=0
            if matches[i][1] not in mps:
                mps[matches[i][1]]=0
            if matches[i][1]  in mps:
                mps[matches[i][1]]+=1
            
        for key,value in mps.items():
            if value == 0:
                zeroloss.append(key)
            elif value == 1:
                oneloss.append(key)
        return [sorted(zeroloss),sorted(oneloss)]
            
        

            
