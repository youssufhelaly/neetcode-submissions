class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        rowd = defaultdict(set)
        cold = defaultdict(set)
        box = defaultdict(set)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                b = (r // 3) + (c // 3) + ((r // 3)*3)
                if board[r][c] in rowd[r]:
                    print("row")
                    return False
                if board[r][c] in cold[c]:
                    print("col")
                    return False
                if board[r][c] in box[b]:
                    print(r)
                    print(c)
                    print(box)
                    print(board[r][c])
                    print("box")
                    return False

                rowd[r].add(board[r][c])
                cold[c].add(board[r][c])
                box[b].add(board[r][c])
                print(box)
        return True
