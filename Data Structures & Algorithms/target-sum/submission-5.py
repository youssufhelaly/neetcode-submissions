class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, curr):
            if (i, curr) in dp:
                return dp[(i,curr)]
            if i == len(nums) and target == curr:
                return 1
            if i >= len(nums):
                return 0
            plus = dfs(i + 1, curr + nums[i])

            sub = dfs(i + 1, curr - nums[i])

            dp[(i, curr)] = plus + sub

            return dp[(i,  curr)]

        total = dfs(0, 0)
        return total