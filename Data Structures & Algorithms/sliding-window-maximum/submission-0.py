class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#Brute force would be to append the max of the sliding window every iteration in a list. I will implement this to see runtime against other algorithms before i try some other approaches i have in mind 
        res = []
        l = 0
        for r in range(k-1,len(nums)):
            res.append(max(nums[l:r+1]))
            l+=1 
        return res 


