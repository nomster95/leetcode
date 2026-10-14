class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        islands = 0
        m , n = len(grid) , len(grid[0])
        def dfs(i,j):
            nonlocal is_closed
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==1:
                return 

            grid[i][j] = 1
            if i==0 or i==m-1 or j==0 or j==n-1:
                is_closed = False

            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    is_closed = True
                    dfs(i,j)

                    if is_closed:
                        islands+=1


        return islands                
        