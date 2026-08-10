class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        prev2,prev1 = cost[0],cost[1]
        for i in range(2,len(cost)):
            cur  = min(prev2,prev1) + cost[i]
            prev2 = prev1 
            prev1 = cur 
        return min(prev2,prev1)