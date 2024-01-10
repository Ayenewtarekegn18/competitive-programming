class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = []
        i = 0
        j = len(p)
        anagram = defaultdict(int)
        temp = defaultdict(int)

        anagram = Counter(p)
        
        if len(p) > len(s):
            return count
        for l in range(0,j):
            temp[s[l]] +=1
        
        if temp == anagram:
            count.append(i)
            
        while j < len(s):
           
            if temp[s[i]] == 1:
                del temp[s[i]]
            else:
                temp[s[i]] -=1
            temp[s[j]] +=1
            
            i+=1
            j+=1
            if temp == anagram:
                count.append(i)
                  
        return count