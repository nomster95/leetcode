from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = [[False]*n for _ in range(m)]
        dist = [[0]*n for _ in range(m)]
        q = deque()

        #add all zeroes as starting points
        #apply multi bfs on them
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    visited[i][j] = True

        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        while len(q)!=0:
            row , col , steps = q.popleft()
            dist[row][col] = steps
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if (0 <= nrow < m and 0 <= ncol < n and not visited[nrow][ncol]):

                    visited[nrow][ncol] = True
                    q.append((nrow,ncol,steps+1))


        return dist             



        


        