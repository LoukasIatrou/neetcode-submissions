class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        # I can set nums into a set so i can look up the element that is one bigger for each instance. Then i can keep a running count and a best count, and return the best count at the end 
        if len(nums)==0:
            return 0
        count,best = 1,0
        seen1 = set(nums)
        for num in nums:
            while ((num+1) in seen1):
                count += 1
                num += 1
            best = max(count,best)
            count  = 1
        return best 