class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def back(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in memo:
                return memo[remaining]
            mini = float('inf')
            for coin in coins:
                mini = min(mini, 1 + back(remaining - coin))
            
            memo[remaining] = mini
            return mini
        res = back(amount)
        return res if res != float('inf') else -1