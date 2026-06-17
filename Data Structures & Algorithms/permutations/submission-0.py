class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        temp = []
        def backtrack(s):
            if len(temp)==len(nums):
                res.append(temp.copy())
                return
            for x in range(len(nums)):
                if nums[x] not in temp:
                    temp.append(nums[x])
                    backtrack(x+1)
                    temp.pop()
        backtrack(0)
        return res
