class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        
        
        
        
        for col_start in range(1,m):
            i = 0
            j = col_start
            ans = []
            while i<n and j<m:
                ans.append(grid[i][j])
                
                i+=1
                j+=1
            ans.sort()
            i = 0
            j = col_start
            k = 0
            while i<n and j<m:
                grid[i][j] = ans[k]
                i+=1
                j+=1
                k+=1



        for row_start in range(n):
            i = row_start
            j=0
            ans = []
            while i<n and j<n:
                ans.append(grid[i][j]) 
                 
                i+=1
                j+=1     
            ans.sort(reverse = True) 
            i = row_start
            j = 0
            k = 0
            while i<n and j<m:
                grid[i][j] = ans[k]
                i+=1
                j+=1
                k+=1

        return grid        


        

            

            
           

