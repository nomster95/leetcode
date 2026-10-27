class Solution:
    def __init__ (self):
        self.count = 0
    def dfs(self,r,c,remaining,grid,m,n):
            if r>=m or r<0 or c>=n or c<0 or grid[r][c]==-1 or grid[r][c]==-2:
                return 

            if grid[r][c]==2:
                if remaining==1:
                    self.count+=1
                return

            original = grid[r][c]
            grid[r][c] = -2

            self.dfs(r,c+1,remaining-1,grid,m,n)
            self.dfs(r+1,c,remaining-1,grid,m,n)
            self.dfs(r,c-1,remaining-1,grid,m,n)
            self.dfs(r-1,c,remaining-1,grid,m,n)

            grid[r][c] = original

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        start_cell = (0,0)
        end_cell = (0,0)
        cells = 0
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    cells+=1
                elif grid[i][j]==1:
                    start_cell = (i,j)
                    cells+=1
                elif grid[i][j]==2:
                    end_cell = (i,j)
                    cells+=1

        self.dfs(start_cell[0],start_cell[1],cells,grid,m,n)   
        return self.count     

        


                                   
                         

        