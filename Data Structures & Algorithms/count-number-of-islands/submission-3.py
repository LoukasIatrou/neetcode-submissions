class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]* cols for _ in range(rows)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(sr,sc):
            stack = [(sr,sc)]
            visited[sr][sc]= True
            while stack:
                r,c = stack.pop()
                for dr,dc in directions:
                    nr,nc = r + dr, c+ dc
                    if 0<=nr<rows and 0<= nc<cols and not visited[nr][nc] and grid[nr][nc]=="1":
                        visited[nr][nc]= True
                        stack.append((nr,nc))
        total = 0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c]=="1":
                    total += 1
                    dfs(r,c)
        return total      