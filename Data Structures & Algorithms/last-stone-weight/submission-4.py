class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        maxheap = stones
        while len(maxheap)>1:
            x = -(heapq.heappop(maxheap))
            y = - (heapq.heappop(maxheap))
            if x==y:
                continue 
            elif x>y:
                heapq.heappush(maxheap,-(x-y))
            else:
                heapq.heappush(maxheap,-(y-x))    
        return -maxheap[0] if len(maxheap)>0 else 0          