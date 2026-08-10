class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        onesrow = []
        onescol = []
        diff = [[0]*m for _ in range(n)]
        for i in range(n):
            count = 0
            for j in range(m):
                if grid[i][j]==1:
                    count+=1
            onesrow.append(count)        

        for i in range(m):
            count = 0
            for j in range(n):
                if grid[j][i]==1:
                    count+=1
            onescol.append(count)  

        for i in range(n):
            for j in range(m):
                rowzeroes = m - onesrow[i]  
                colzeroes = n - onescol[j]   

                diff[i][j] = onesrow[i] + onescol[j] - rowzeroes - colzeroes

        return diff        
        
