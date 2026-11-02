class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        def dfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == '1' and (nr,nc) not in visited:
                    dfs(nr, nc)

    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row,col) not in visited:
                    dfs(row, col)
                    islands += 1

        return islands

        


