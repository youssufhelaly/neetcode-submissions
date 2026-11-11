class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        res = ''
        counter = 0
        m = ''
        l = ''
        print(max(count))

        if max(count.values()) > (len(s) + 2 - 1) // 2:
            return ''
        while counter != len(s):
            m = max(count, key=count.get)
            print(m)
            res += m
            count[m] -= 1
            print(count)
            if l:
                count[l] = -count[l]
            count[m] = -count[m]

            print(count)
            counter += 1 
            l = m
        return res
