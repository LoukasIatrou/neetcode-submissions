class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I want to create hash maps that keep count of the strings 
        # and compare them to the. Keeping the count of all the 
        # substrings and tracking could easily break down at large scale 
        # We could also set an array of legth 26 and keep track if any of 
        # the current words satisfy the same count as the previous one 
        res = defaultdict(list)
        for s in strs:
            count = [0]*26 
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            print(res.values)
        return list(res.values())