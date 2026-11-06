class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        boole = False
        visitor = set()
        def dfs(r, c, i):
            nonlocal boole

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if i >= len(word):
                return False
            if (r,c) in visitor:
                return False
            if word[i] != board[r][c]:
                return False
            if i == len(word) - 1:
                return True
            visitor.add((r,c))

            if word[i] == board[r][c]:
                found = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1) or dfs(r - 1, c, i + 1)   
            visitor.remove((r,c))
            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visitor and word[0] == board[r][c]:
                    if dfs(r, c, 0):
                        return True
        return False