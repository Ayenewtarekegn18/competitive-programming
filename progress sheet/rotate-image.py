class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r= len(matrix)-1
        while (l<r):
            matrix[l],matrix[r] =  matrix[r],matrix[l]
            l+=1
            r-=1
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                if i < j :
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                    print(matrix)

        