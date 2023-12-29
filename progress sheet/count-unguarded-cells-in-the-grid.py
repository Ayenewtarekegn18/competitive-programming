class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guard = set()
        for i in guards:
            guard.add(tuple(i))
        wall = set()
        for i in walls:
            wall.add(tuple(i))

        grid = [[0  for _ in range(n)] for _ in range(m)]
        ans = 0
        for row in range(m):
            for col in range(n):
                if (row,col) in guard:
                    i = row
                    j = col
                    while (i,j) not in wall and j < n: # horizontal right
                        grid[i][j] = 1
                        j +=1
                        if (i,j) in guard:
                            break
                    if j < n or (i,j) in wall:
                        grid[i][j] = 1
                    i = row
                    j = col
                    while (i,j) not in wall and j >= 0: # horizontal left
                        grid[i][j] = 1
                        j-=1
                        if (i,j) in guard:
                            break
                    if j >= 0 or (i,j) in wall:
                        grid[i][j] = 1
                    i = row
                    j = col
                    while (i,j) not in wall and i < m: # vertical down
                        grid[i][j] = 1
                        i +=1
                        if (i,j) in guard:
                            break
                    if i < m or (i,j) in wall:
                        grid[i][j] = 1
                    i = row
                    j = col
                    while (i,j ) not in wall and i >= 0: # vertical up
                        grid[i][j] = 1
                        i -= 1
                        if (i,j) in guard:
                            break
                    if i >= 0 or (i,j) in wall:
                        grid[i][j] = 1
                elif (row,col) in wall:
                    grid[row][col] = 1
                    
        print(grid)
        # print(wall)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    ans+=1
        return ans