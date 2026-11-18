class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr)
                return
            for num in nums:
                if num not in curr:
                    tmp = curr.copy()
                    tmp.append(num)
                    print(curr)
                    dfs(tmp)

        dfs([])
        return res