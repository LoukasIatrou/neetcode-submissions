class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = {}
            for c in s:
                count[c] = count.get(c,0) + 1
            key = tuple(sorted(count.items()))
            res[key].append(s)
        return list(res.values())