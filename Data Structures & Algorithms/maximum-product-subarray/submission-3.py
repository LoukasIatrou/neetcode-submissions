class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        curMax,curMin = 1,1
        for num in nums:
            oldMax,oldMin = curMax,curMin
            
            curMax = max(num,oldMax*num,oldMin*num)
            curMin = min(num,oldMax*num,oldMin*num)
            best = max(curMax,best)
        return best 

        #we need to take into consideration that we can have the running sum be negative and then 
        #so we must also cosnider the running negative product
