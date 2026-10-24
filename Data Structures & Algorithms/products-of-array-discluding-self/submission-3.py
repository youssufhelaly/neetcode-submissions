class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        curr = 1
        for num in nums[:-1]:
            curr *= num
            left.append(curr)
        curr = 1
        for i in range(len(left) - 1,-1,-1):
            left[i] *= curr
            curr *= nums[i]
        return left