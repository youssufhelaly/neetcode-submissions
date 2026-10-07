class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a) - 1
        m = len(b) - 1
        res = ''
        rest = 0
        while n != -1 or m != -1:
            num = rest
            if n >= 0:
                num += int(a[n])
                n -= 1
            if m >= 0:
                num += int(b[m])
                m -= 1
            res = str(num%2) + res
            rest = num // 2
        if rest:
            res = '1' + res
        return res
