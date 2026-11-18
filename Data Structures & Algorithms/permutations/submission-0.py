class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        left = set(nums)
        def dfs(curr, left):
            if not left:
                res.append(curr)
                return
            for num in left:

                l = left.copy()
                l.remove(num)
                tmp = curr.copy()
                tmp.append(num)
                print(curr)
                print(left)
                dfs(tmp, l)

        dfs([], nums)
        return res