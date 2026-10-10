class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l = 0
        r = 0
        res = float('-inf')
        curr = 0
        while l <= r and r<len(nums):
            curr += nums[r]
            res = max(res, curr)
            if curr < 0:
                l = r
                curr=0
            r += 1

        return res