class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows , Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        INF = 2147483647
        q = deque()
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0<=nr<Rows and 0<=nc<Cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))

