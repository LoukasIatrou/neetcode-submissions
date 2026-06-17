class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = isConnected
        n = len(isConnected)
        visited = [False] * n
        def dfs(s):
            visited[s]= True
            stack = [s]
            while stack:
                u = stack.pop()
                for v in range(n):
                    if not visited[v] and adj[u][v]==1:
                        visited[v] = True
                        stack.append(v)
        total = 1
        dfs(0)
        for i in range(n):
            if not visited[i]:
                total +=1 
                dfs(i)
        return total
   