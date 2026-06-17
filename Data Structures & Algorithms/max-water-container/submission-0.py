class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cnt = 0
        l,r = 0, len(heights)-1
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            max_cnt = max(area,max_cnt)
            if heights[l]<=heights[r]:
                l += 1
            else:
                r -= 1
        return max_cnt


            

        