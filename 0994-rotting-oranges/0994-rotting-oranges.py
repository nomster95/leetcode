from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        empty , fresh , rotten = 0 , 1 , 2
        m , n = len(grid) , len(grid[0])
        num_fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==rotten:
                    q.append((i,j))
                elif grid[i][j]==fresh:
                    num_fresh+=1

        if num_fresh==0:
            return 0

        minutes = -1
        while q:
            q_size = len(q)
            minutes+=1
            for _ in range(q_size):
                i , j = q.popleft()
                for r,c in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==fresh:
                        grid[r][c]= rotten
                        num_fresh-=1
                        q.append((r,c))

        if num_fresh==0:
            return minutes
        else:
            return -1                    

