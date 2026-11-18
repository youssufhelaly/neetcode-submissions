from bisect import insort
class TimeMap:

    def __init__(self):
        self.emotions = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.emotions[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if self.emotions[key]:
            values = self.emotions[key]
            if values[0][1] > timestamp:
                return ''
            l, r = 0, len(values) - 1
            while l < r:
                m = (l + r) // 2
                curr = values[m][1]

                if curr == timestamp:
                    return values[m][0]
                elif curr < timestamp:
                    l = m + 1
                else:
                    r = m - 1
            if values[l][1] > timestamp:
                l -= 1
            return values[l][0]
        else:
            return ''
