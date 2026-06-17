class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        temp = []
        used=[False]*len(nums)
        def backtrack():
            if len(temp)==len(nums):
                res.append(temp.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue 
                used[i] = True
                temp.append(nums[i])
                backtrack()
                temp.pop()
                used[i] = False
        backtrack()
        return res
                