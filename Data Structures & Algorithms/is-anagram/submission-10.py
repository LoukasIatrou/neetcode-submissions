class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = {}, {}
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i],0) + 1
        for j in range(len(t)):
            t_count[t[j]] = t_count.get(t[j],0) + 1
        if s_count == t_count:
            return True
        return False