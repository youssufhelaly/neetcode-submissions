class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 2)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n + 2):
            dp[i] = dp[i-1] + dp[i -2]
        print(dp)
        return dp[n + 1]