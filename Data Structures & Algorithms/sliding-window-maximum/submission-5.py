class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#Brute force would be to append the max of the sliding window every iteration in a list. I will implement this to see runtime against other algorithms before i try some other approaches i have in mind 
        '''
        res = []
        l = 0
        for r in range(k-1,len(nums)):
            res.append(max(nums[l:r+1]))
            l+=1 
        return res 
        '''
#This solution worst case when k is big leads to pretty bad runtime because we iterate through the whole k window everytime.
# We can keep a stack with the biggest element in the current window, let me try that
        '''
        res, stack = [],[]
        stack.append(max(nums[:k]))
        res.append(stack[-1])
        print(stack)
        l = 0 #We already covered the first window hence we start from the second window
        for r in range(k,len(nums)):
            if nums[l]==stack[-1]:
                stack.pop()
            l += 1
            if stack and nums[r]>stack[-1]:
                stack.append(nums[r])
            res.append(stack[-1])
            print(res)
        return res 
        '''
#Nromal Stack doesnt work here, hence a heapq  should work. This gives O(nlog(n)) complecity
        '''
        import heapq 
        max_heap = [] 
        res = []
        for r in range(len(nums)):
            # Push the rth element into our max heap 
            heapq.heappush(max_heap,[-nums[r],r])
            # Pop the elements outside our sliding window
            while max_heap and max_heap[0][1]<= (r-k):
                heapq.heappop(max_heap)
            # Now we append the biggest element in our result array
            if (r+1)>= k:
                res.append(-max_heap[0][0])
        return res 
        '''
#However we can do better by using a deque
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
        




