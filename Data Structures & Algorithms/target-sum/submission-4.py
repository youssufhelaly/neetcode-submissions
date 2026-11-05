class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, curr):
            if (i, curr) in dp:
                return dp[(i,curr)]

            if i == len(nums) - 1 and target == curr:
                return 1
            if i + 1 >= len(nums):
                return 0
            plus = dfs(i + 1, curr + nums[i + 1])

            sub = dfs(i + 1, curr - nums[i + 1])

            dp[(i, curr)] = plus + sub

            return dp[(i,  curr)]

        total = dfs(0, -nums[0]) + dfs(0, nums[0])
        return total