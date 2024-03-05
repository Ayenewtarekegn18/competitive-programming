class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        path =set()

        def backtrack(r,c,i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r == row or c == col 
                or (r,c) in path or board[r][c] != word[i]):
                return False
            
            path.add((r,c))

            result = backtrack(r+1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1)

            path.remove((r,c))

            return result
        for rows in range(row):
            for cols in range(col):
                if backtrack(rows,cols,0):
                    return True
        return False