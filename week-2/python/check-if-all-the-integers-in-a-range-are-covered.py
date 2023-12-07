class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range (left,right+1):
            flag = False
            for j in ranges:
                if i >= j[0] and i <= j[1]:
                    flag = True
            if flag == False:
                return flag
        return True 
        