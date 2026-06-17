class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(i,n):
            if len(temp)==n:
                res.append(temp.copy())
                return 

            for x in range(i, len(nums)):
                temp.append(nums[x])
                backtrack(x+1,n)
                temp.pop()

        for i in range(len(nums)+1):
                backtrack(0,i)
        return res        