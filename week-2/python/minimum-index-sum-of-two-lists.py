class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minsum=10000
        anslist=[]
        for i in list1:
            if i in list2:
                indexsum = list1.index(i) + list2.index(i)
                if minsum > indexsum:
                    minsum = indexsum
                    anslist=[i]
                elif minsum == indexsum:
                    anslist.append(i)
        return anslist

        return 

                    
        