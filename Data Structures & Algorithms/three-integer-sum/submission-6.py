class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        # now we have the sorted numbers we can fix one number and use two pointers to 
        # to try and find the the 2 sum that matched the fixed one 
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate fixed values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since nums is sorted, if nums[i] > 0,
            # all future values are also positive.
            if nums[i] > 0:
                break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
