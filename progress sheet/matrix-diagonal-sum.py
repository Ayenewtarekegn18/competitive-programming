class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        j = 0
        primary_diagonal = 0
        secondary_diagonal = 0

        while(i<len(mat) and j<len(mat)):
            primary_diagonal += mat[i][j]
            i+=1
            j+=1

        j = 0
        i = len(mat)-1
        while(i >= 0 and j < len(mat)):
            primary_diagonal += mat[i][j]
            i-=1
            j+=1

        if len(mat)%2 == 1 :
            return primary_diagonal + secondary_diagonal - mat[len(mat)//2][len(mat)//2]
        else:
            return primary_diagonal + secondary_diagonal 

        

            
            
        