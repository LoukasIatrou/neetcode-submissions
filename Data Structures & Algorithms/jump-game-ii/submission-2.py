class Solution:
    def jump(self, nums: List[int]) -> int:
        goal, reach = len(nums)-1 , nums[0]
        if goal ==  0:
            return 0
        l,r = 0,reach
        count = 1
        while r < goal:
            #Iterate through our range of values
            reach = 0
            for i in range(l,r+1):
                reach = max(reach, (i+nums[i]))
            count +=1 
            l = r
            r = reach 
        return count 