class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        anagram = defaultdict(int)
        temp = defaultdict(int)

        anagram = Counter(s1)
        
        if len(s1) > len(s2):
            return False
        for l in range(0,j):
            temp[s2[l]] +=1
        
        if temp == anagram:
            return True
            
        while j < len(s2):
           
            if temp[s2[i]] == 1:
                del temp[s2[i]]
            else:
                temp[s2[i]] -=1
            temp[s2[j]] +=1
            
            i+=1
            j+=1
            if temp == anagram:
                return True
                  
        return False