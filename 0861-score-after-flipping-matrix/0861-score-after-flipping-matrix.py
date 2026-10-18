class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        total = 0
        # check rows
        for i in range(n):
            if grid[i][0]==0:
                for j in range(m):
                    if grid[i][j]==0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0

        #check cols                
        for i in range(m):
            zeroes = 0
            ones = 0
            for j in range(n):
                if grid[j][i]==0:
                    zeroes+=1
                else:
                    ones+=1

            if zeroes>ones:
                for j in range(n):
                    if grid[j][i]==0:
                        grid[j][i] = 1
                    else:
                        grid[j][i] = 0

        for x in grid:
            ans = ""
            for y in x:
                ans+=str(y)

            total+=int(ans,2)

        return total        



        