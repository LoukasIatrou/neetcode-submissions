class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        total = 0
        def backtrack(s,total):
            if total == target:
                res.append(temp.copy())
                return 
            for x in range(s,len(candidates)):
                new_total =total+ candidates[x]
                if new_total>target:
                    continue
                temp.append(candidates[x])
                backtrack(x,new_total)
                temp.pop()
        backtrack(0,0)
        return res     