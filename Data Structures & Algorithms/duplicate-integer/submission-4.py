class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = []
        for x in nums:
            if x in dups:
                return True
            dups.append(x)
        return False
        