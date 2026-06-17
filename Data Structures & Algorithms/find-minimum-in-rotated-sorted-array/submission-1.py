class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return none
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[r]:
                l = mid + 1
            if nums[mid]<nums[r]:
                r = mid -1 
            
                