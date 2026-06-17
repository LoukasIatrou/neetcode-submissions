class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visited = [[False]* cols for _ in range(rows)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(sr,sc):
            global area
            area = 1
            stack = [(sr,sc)]
            visited[sr][sc]= True
            while stack:
                r,c = stack.pop()
                for dr,dc in directions:
                    nr,nc = r + dr, c+ dc
                    if 0<=nr<rows and 0<= nc<cols and not visited[nr][nc] and grid[nr][nc]==1:
                        visited[nr][nc]= True
                        area += 1
                        stack.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c]==1:
                    dfs(r,c)
                    max_area = max(max_area,area)
        return max_area        