class Solution:
    def minWindow(self, s: str, t: str) -> str:
# In this iteration we are looking for permutations, rather we are looking for all the characters that exist in
# the substring. 
# What should my stopping condition be. When should we increment the left pointer?
        count = {}
        for char in t:
            count[char] = count.get(char,0) + 1 
        l = r = have  = 0
        best = float('inf')
        Lbest, Rbest = 0,0
        need = len(count)
        seen = {}
        while r<len(s):
            seen[s[r]] = seen.get(s[r],0)+1
            if s[r] in count and seen[s[r]]==count[s[r]]:
                have +=1 
            print(s[l:r+1])
            while have == need:
                if best > (r-l+1):
                    Lbest,Rbest = l,r 
                    best = (r-l+1)
                seen[s[l]] -= 1
                if (s[l] in count) and seen[s[l]]<count[s[l]]:
                    have -=1 
                    print(have)
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l +=1 
            r += 1
        return s[Lbest:Rbest+1] if best!= float('inf') else ""

