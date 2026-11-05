class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 0
        dp = {}
        def dfs(r, c):
            nonlocal result
            if (r,c) in dp :
                return dp[r,c]
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0 
            if r == (m - 1) and c == (n - 1):
                return 1
            
            ri = dfs(r + 1, c)
            le = dfs(r, c + 1)
            dp[(r,c)] =  ri + le
            print(dp[r,c])
            return dp[r,c]

        return dfs(0,0)

