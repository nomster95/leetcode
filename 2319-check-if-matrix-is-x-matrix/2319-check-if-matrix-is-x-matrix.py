class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        x_matrix = True
        for i in range(n):
            for j in range(m):
                if i==j or i==n-1-j:
                    if grid[i][j]==0:
                        x_matrix = False
                if i!=j and i!=n-1-j:
                    if grid[i][j]!=0:
                        x_matrix = False
                        
        return x_matrix                      

        