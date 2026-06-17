class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current,best = nums[0],nums[0]
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            current = max(current+nums[i],nums[i])
            best = max(current,best)
        return best