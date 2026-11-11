class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        res = ''
        m = ''
        l = ''

        for _ in range(len(s)):
            m = max(count, key=count.get)
            if count[m] <= 0:
                break
            res += m
            count[m] -= 1
            if l:
                count[l] = -count[l]
            count[m] = -count[m]
            l = m
        return res if len(res) == len(s) else ''
