class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        rest = []
        for i in arr1:
            if i in freq:
               freq [i] += 1
            else:
                freq[i] = 1
        k = 0
        for j in arr2:
            while freq[j] != 0:
                arr1[k] = j
                k +=1
                freq[j] -= 1 
            del freq[j]
        for key , val in freq.items():
            while val != 0:
                rest.append(key)
                val -= 1 
        rest.sort()
        for n in rest:
            arr1[k] = n  
            k += 1      
        return arr1