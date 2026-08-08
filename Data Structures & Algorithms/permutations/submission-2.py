class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        def backtrack(i,cur):
            if len(cur)==len(nums):
                res.append(cur.copy())
            for i in range(len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    cur.append(nums[i])
                    backtrack(i+1,cur)
                    seen.remove(nums[i])
                    cur.pop()
        backtrack(0,[])
        return res 