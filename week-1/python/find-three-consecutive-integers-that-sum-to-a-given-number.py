class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # i=0
        # j=1
        # k=2
        # while i+j+k<=num:
        #     if i+j+k==num:
        #         return [i,j,k]
        #     i+=1
        #     j+=1
        #     k+=1
        # else:
        #     return[]
        x=num//3
        if x-1 + x + x+1==num:
            return [x-1,x,x+1]
        else :
            []