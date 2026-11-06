class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        seen = defaultdict(int)
        m = 0
        res = 0
        while l <= r and r < len(s):
            length = r - l + 1
            seen[s[r]] += 1
            m = max(seen[s[r]], m)

            if length - m > k:
                print(s[r])
                seen[s[l]] -= 1

                l += 1
            else:
                res = max(res, length)
            r += 1
        
        return res