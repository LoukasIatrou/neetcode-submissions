class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
# Brute force means iterating for every possible substring of length equal to s1 and checking counts mannually 
# this means O(n^2) due to the nested loop 
        count = {}
        #Initiate the count hash table we use to track string 1 
        for s in s1:
            count[s] = count.get(s,0) + 1
        l,r = 0, 0
        seen = {}
        while r < len(s2):
            seen[s2[r]] = seen.get(s2[r],0)+1
            if (r-l+1) == len(s1):
                if seen == count:
                    return True
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l +=1 
            r += 1 
        return False


        
 