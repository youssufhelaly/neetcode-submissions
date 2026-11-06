class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        sorted_seen = sorted(seen.items(), key=lambda x:x[1], reverse= True)


        res = []
        for num, freq in sorted_seen[:k]:
            res.append(num)

        return res