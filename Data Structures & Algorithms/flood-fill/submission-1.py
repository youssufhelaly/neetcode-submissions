class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        original = image[sr][sc]
        image[sr][sc] = color
        visited = set()

        def dfs(sr, sc):
            if (sr, sc) in visited:
                return
            visited.add((sr,sc))
            DIR = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr,dc in DIR:
                nr, nc = dr + sr, dc + sc
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == original:
                    image[nr][nc] = color
                    dfs(nr,nc)

        dfs(sr,sc)
        return image
