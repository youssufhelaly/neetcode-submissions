class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = float('-inf')
        dp = {}

        def dfs(i, j):
            three = 0
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in dp:
                return dp[i, j]
            if text1[i] == text2[j]:
                three = dfs(i + 1, j + 1) + 1
            one = dfs(i + 1, j)
            two = dfs(i, j + 1)
            dp[(i,j)] = max(one, two)
            if three:
               dp[(i,j)] = max(dp[(i,j)], three) 
            return dp[(i, j)]
        return dfs(0,0)
                