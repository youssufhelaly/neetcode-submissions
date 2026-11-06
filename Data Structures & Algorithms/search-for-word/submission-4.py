class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        boole = False
        visitor = set()
        def dfs(r, c, i):
            nonlocal boole

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if i >= len(word):
                return
            if (r,c) in visitor:
                return 
            if word[i] != board[r][c]:
                return
            if i == len(word) - 1:
                boole = True
                return
            visitor.add((r,c))

            if word[i] == board[r][c]:
                dfs(r + 1, c, i + 1)
                dfs(r, c + 1, i + 1)
                dfs(r, c - 1, i + 1)
                dfs(r - 1, c, i + 1)   
            visitor.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visitor and word[0] == board[r][c]:
                    dfs(r, c, 0)
        return boole