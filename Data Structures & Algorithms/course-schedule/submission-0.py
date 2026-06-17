class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            neighbors[b].append(a)
        state = [0]*numCourses
        def dfs(u):
            if state[u]==1:
                return False
            if state[u]==2:
                return True
            state[u]=1
            for v in neighbors[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True
        for i in range(numCourses):
            if state[i]==0:
                if not dfs(i):
                    return False
        return True        