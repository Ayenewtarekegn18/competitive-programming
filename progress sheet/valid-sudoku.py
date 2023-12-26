class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sub_box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                elif (board[i][j] in row[i] or
                    board[i][j] in col[j] or 
                    board[i][j] in sub_box[ ( i//3 , j//3 ) ] ):
                    return False  
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                sub_box[( i//3, j//3) ].add(board[i][j])
        return True
        