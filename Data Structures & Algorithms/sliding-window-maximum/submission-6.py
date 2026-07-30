class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        from collections import deque 
        q = deque()
        res = []
        for r in range(len(nums)):
            while q and q[0]<= (r-k):
                q.popleft()
            while q and nums[q[-1]]<=nums[r]:
                q.pop()
            q.append(r)
            if r+1>=k:
                res.append(nums[q[0]])
        return res 
        




