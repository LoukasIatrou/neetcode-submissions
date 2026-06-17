class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)
        i=1
        k=0
        r=-1
        n = len(nums)
        while k<n:
            if i!=n and i>=k+1:
                out[k]*=nums[i]
                i += 1
            elif r != -1 and r<= k-1:
                out[k]*=nums[r]
                r -=1 
            if i == n and r==-1:
                k +=1 
                i = k +1
                r = k-1 
        return out
