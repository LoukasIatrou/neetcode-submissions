class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows,Cols = len(board), len(board[0])
        seen = set()
        def dfs(r,c,i):
            if (r<0 or c<0 or r==Rows or c==Cols or word[i]!=board[r][c] or (r,c) in seen):
                return 
            if i == len(word)-1 and board[r][c]==word[i]:
                return True
            seen.add((r,c))
            found = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            if found == True:
                return True
            seen.remove((r,c))
        for r in range(Rows):
            for c in range(Cols):
                if dfs(r,c,0)==True:
                    return True
        return False
        
            