class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        total = 0
        for i, num in enumerate(nums):
            r = len(nums) - 1
            if i > 0 and num == nums[i - 1]:
                continue
            l = i + 1
            while l < r:
                total = num + nums[l] + nums[r]
                if (total) == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while r >= 0 and r < (len(nums) - 1) and nums[r] == nums[r + 1]:
                            r -= 1

                    while l > 0 and l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res
