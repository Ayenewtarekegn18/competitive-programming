class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0 for _ in range(1001)]
        for i in trips :
            prefix[i[1]] +=i[0]
            prefix [i[2]] -=i[0]
        total= 0 
        for j in range(len(prefix)):
            total += prefix[j]
            prefix[j] = total
        for k in prefix:
            if k > capacity :
                return False
        return True

            
