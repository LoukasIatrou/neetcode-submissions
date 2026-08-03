class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#Lets attempt to treat the arr as a linked list where i is pointing to nums[i]
        s,f= 0,0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s==f:
                #We found the cycle, and from this point we can implement another slow pointer because we know from the idx they match onwards we have a duplicate char. 
                s2 = 0
                while s!=s2:
                    s = nums[s]
                    s2 = nums[s2]

                return s
        
            
            

