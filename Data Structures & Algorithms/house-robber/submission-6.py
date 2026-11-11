class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        print(dp)
        for i, num in enumerate(nums):   
            print(num)
            # rob
            rob = dp[i - 2] + num
            # skip
            skip = dp[i-1]

            dp[i] = max(rob, skip)

        print(dp)
        return dp[-3]