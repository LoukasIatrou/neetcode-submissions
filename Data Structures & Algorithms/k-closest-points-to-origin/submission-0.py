import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        res = []
        for x,y in (points):
            dist = math.sqrt((x)**2 + (y)**2)
            distance.append([dist,(x,y)])
        heapq.heapify(distance)
        for _ in range(k) :
            val = heapq.heappop(distance)
            res.append(val[1])
        return res 