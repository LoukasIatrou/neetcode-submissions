class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We want to return the indices, maybe we create a list with remainders and 
        # and then search for the single element that completes to 0 and add it within 
        # a list of indices
        total = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in total:
                return [total[difference],i]
            total[nums[i]] = i 
        return []
