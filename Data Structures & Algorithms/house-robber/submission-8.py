class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) )

        def dfs(i, robbed):   
            if i >= len(nums):
                return 0
            
            # rob
            if robbed:
                return dfs(i + 1, False)

            else:
                if dp[i] != -1:
                    return dp[i]
                rob = dfs(i + 1, True)
                # skip
                skip = dfs(i + 1, False)
                dp[i] = max(rob + nums[i], skip)
                return dp[i]

        dfs(0, False)
        return dp[0]