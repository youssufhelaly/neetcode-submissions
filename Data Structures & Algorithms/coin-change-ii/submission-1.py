class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        def dfs(i, curr):
            if (curr, i) in dp:
                return dp[(curr, i)]
            if curr < 0:
                return 0
            if curr == 0:
                return 1
            if i >= len(coins):
                return 0
            use = dfs(i, curr - coins[i])
            skip = dfs(i + 1, curr)
            dp[(curr, i)] = use + skip
            return dp[(curr, i)]
        return dfs(0, amount)