class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if i >= len(nums):
                return
            if total > target:
                return
            if total == target:
                res.append((curr))
                return
            
            # skip
            dfs(i+1, curr, total)
            new = curr.copy()
            new.append(nums[i])

            # go
            dfs(i, new, total + nums[i])
        dfs(0, [], 0)
        return res
        
        

        
