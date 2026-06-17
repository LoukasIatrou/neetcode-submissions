class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==0:
            return -1
        if grid[0][0] == 1 or grid[n-1][n-1]== 1:
            return -1
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        q = deque()
        q.append((0,0,1))
        visited = [[False]*n for _ in range(n)]
        visited[0][0]= True
        while q:
            r,c,dist = q.popleft()
            print(r,"",c,"",dist)
            if r==(n-1) and (c==n-1):
                return dist
            for dr,dc in directions:
                nr,nc = r + dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc,dist+1))
        return -1




        
        