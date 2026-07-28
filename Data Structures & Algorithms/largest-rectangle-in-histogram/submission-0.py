class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0 
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]> h: 
                idx, height = stack.pop()
                best = max(best, (height*(i-idx)))
                start = idx
            stack.append((start,h))
        print(stack)
        for i, h in stack:
            best = max(best,h * (len(heights)-i))

        return best