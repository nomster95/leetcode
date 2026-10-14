class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        sub_islands = 0
        m , n = len(grid2) , len(grid2[0])
        def dfs(i,j):
            nonlocal is_sub
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0:
                return 

            grid2[i][j] = 0     
            
            if grid1[i][j]==0:
                is_sub = False

            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)


        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    is_sub = True
                    dfs(i,j)
                    
                    if is_sub:
                        sub_islands+=1


        return sub_islands            

        


        