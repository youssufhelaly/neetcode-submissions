class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = defaultdict(int)
        dictt = defaultdict(int)
        n = len(s)
        m = len(t)
        if n != m:
            return False
        for i in range(n):
            dicts[s[i]] += 1
            dictt[t[i]] += 1
        return dicts == dictt