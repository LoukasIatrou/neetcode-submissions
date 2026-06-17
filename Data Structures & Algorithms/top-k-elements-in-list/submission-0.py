class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for x in nums:
            cnt[x]+=1
        buckets = [[]for _ in range(len(nums)+1)]
        for x,c in cnt.items():
            buckets[c].append(x)
        out = []
        for c in range(len(nums), 0, -1):
            for x in buckets[c]:
                out.append(x)
                if len(out) == k:
                    return out
        return out