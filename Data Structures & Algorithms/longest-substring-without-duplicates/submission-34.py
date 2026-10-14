class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ml = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                ml = max(ml, (r-l + 1))
            else:   
                while l < r:
                    if s[l] != s[r]:
                        seen.remove(s[l])
                        l += 1
                    else:
                        l += 1
                        break
        return ml
