class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid) 
        COLS = len(grid[0])
        visited = set()
        res = 0
        def dfs(r,c):
            nonlocal curr
            if (r, c) in visited:
                return
            visited.add((r,c))
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                curr += 1
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr = 0
                    dfs(r,c)
                    res = max(curr, res)

        return res


