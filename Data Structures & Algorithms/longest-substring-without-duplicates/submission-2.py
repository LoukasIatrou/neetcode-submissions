class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_count = 0
        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l +=1
            seen.add(ch)
            max_count = max(max_count,r-l+1)
        return max_count



