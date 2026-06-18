class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Brute force would be to go over all the lists and keep track of smallest start and overlapping end
        # That would be O(n^2)
        # nlogn runtime hints at a sorting solution based on the first index and compare
        # With second index 
        intervals.sort()
        merged = []
        for start,end in intervals:
            if not merged or start>merged[-1][1]:
                merged.append([start,end])
            else:
                merged[-1][1] = max(merged[-1][1],end)
        return merged

