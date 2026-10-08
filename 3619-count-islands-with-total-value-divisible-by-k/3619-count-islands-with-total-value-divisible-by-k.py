class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0

            island = grid[i][j]    
            grid[i][j] = 0

            return island + dfs(i,j+1) + dfs(i+1,j) + dfs(i,j-1) + dfs(i-1,j)    


        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    area = dfs(i,j)
                    if area%k==0:
                        ans+=1
                    


        return ans          
        
        
        