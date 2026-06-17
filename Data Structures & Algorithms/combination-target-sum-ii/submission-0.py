class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        temp = []
        total = 0
        def backtrack(s,total):
            if total == target and temp not in res:
                res.append(temp.copy())
                return 
            for x in range(s,len(candidates)):
                new_total =total+ candidates[x]
                if new_total>target:
                    break
                temp.append(candidates[x])
                backtrack(x+1,new_total)
                temp.pop()
        backtrack(0,0)
        return res
     