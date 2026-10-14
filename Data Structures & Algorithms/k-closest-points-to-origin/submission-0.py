class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        math = {}
        x2 = 0
        y2 = 0
        for x1, y1 in points:
            res = (((x1 - x2)**2 + (y1 - y2)**2)**0.5)
            math[(x1,y1)] = res
        

        sorted_math = dict((sorted(math.items(), key=lambda item: item[1])))
        final = []
        curr = 0
        for x, y in sorted_math:
            if k == 0:
                break
            final.append((x,y))
            k -= 1

        return final