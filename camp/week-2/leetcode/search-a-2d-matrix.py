class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for cole in range(len(matrix[0])):
                if matrix[row][0] <= target <= matrix[row][-1]:
                    l = 0
                    r = len(matrix[0]) - 1
                    while l <=r :
                        mid = (l + r ) // 2
                        if matrix[row][mid] == target:
                            return True
                        elif matrix[row][mid] > target:
                            r = mid -1
                        else:
                            l = mid + 1
                break
        return False