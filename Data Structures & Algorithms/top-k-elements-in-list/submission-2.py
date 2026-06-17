class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1 
        for _ in range(k):
            best = max(count, key=count.get)
            res.append(best)
            del count[best]
        return res 