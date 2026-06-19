class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i,j in intervals:
            if not merged or i>merged[-1][1]:
                merged.append([i,j])
            else:
                merged[-1][1] = max(merged[-1][1],j)
        return merged


