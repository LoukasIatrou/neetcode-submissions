class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        row, column = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def bfs(r, c):

            queue = collections.deque()
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            queue.append((r, c))

            while queue:
                r_curr, c_curr = queue.pop()

                for dr, dc in directions:
                    r_new, c_new = r_curr + dr, c_curr + dc
                    if (r_new, c_new) not in seen and (r_new in range(row)) and (c_new in range(column)) and grid[r_new][c_new] == '1':
                        queue.append((r_new, c_new))
                        seen.add((r_new, c_new))

        for r in range(row):
            for c in range(column):

                if grid[r][c] == '1' and (r, c) not in seen:

                    seen.add((r, c))
                    islands += 1

                    bfs(r, c)

        return islands

        