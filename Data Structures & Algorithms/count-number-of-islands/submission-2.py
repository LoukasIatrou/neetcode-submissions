class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(sr,sc):
            stack = [(sr,sc)]
            visited[sr][sc]= True
            while stack:
                r,c=stack.pop() 
                for dr,dc in dirs:
                    nr, nc = r +dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc]=="1" and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and not visited[r][c]:
                    islands += 1
                    dfs(r,c)

        return islands        