class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for char in s:
            if char in seen:
                res += 2
                seen.remove(char)
            else:
                seen.add(char)

        return res + 1 if seen else res                