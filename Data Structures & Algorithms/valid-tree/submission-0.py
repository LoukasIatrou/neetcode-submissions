class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= n-1:
            return False
        neighbors = [[] for _ in range(n)]
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        visited = [False] * n
        def dfs(s):
            stack = [s]
            visited[s] = True
            while stack:
                u = stack.pop()
                for v in neighbors[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            return visited
        dfs(0)
        for x in visited:
            if not x:
                return False
        return True    