class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = [[] for _ in range(n)]
        visited = [False]*n
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        def dfs(s,neighbors):
            visited[s]=True
            stack = [s]
            while stack:
                u = stack.pop()
                for v in neighbors[u]:
                    if not visited[v]:
                        visited[v]=True
                        stack.append(v)
        dfs(0,neighbors)
        total = 1
        for i in range(n):
            if not visited[i]:
                total += 1
                dfs(i,neighbors)
        return total 
        