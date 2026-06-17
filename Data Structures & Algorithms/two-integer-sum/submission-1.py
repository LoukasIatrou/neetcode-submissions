class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = {}
        for v,k in enumerate(nums):
            total[k]=v
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in total and total[diff]!=i:
                return [i,total[diff]]
        return []


        
        