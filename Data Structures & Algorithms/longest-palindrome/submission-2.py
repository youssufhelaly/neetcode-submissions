class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        total= 0
        for char in count:
            if count[char] % 2 == 0:
                total += count[char]
            else:
                total += count[char] - 1
        if total == len(s):
            return total
        elif total < len(s):
            return total + 1