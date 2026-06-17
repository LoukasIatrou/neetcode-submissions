class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = [[] for _ in range(n)]
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        visited= [False]*n
        def dfs(s):
            stack = [s]
            visited[s]=True
            while stack:
                u = stack.pop()
                for v in neighbors[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
        total = 0
        for i in range(n):
            if not visited[i]:
                total+=1
                dfs(i)
        return total
            