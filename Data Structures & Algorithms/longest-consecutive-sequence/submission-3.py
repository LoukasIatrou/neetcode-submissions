class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for x in s:
            if x-1 not in s:
                print(x)
                length = 1 
                cur = x
                while (cur + 1) in s:
                    length += 1
                    cur += 1
                    print(length,"l", cur, "c")
                longest = max(longest,length)
        return longest 


            