class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        firstRow = -1
        firstCol = -1
        lastRow = 1
        lastCol = 1

        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if firstRow==-1:
                        firstRow = i

                    lastRow = i

        for j in range(m):
            for i in range(n):
                if grid[i][j]==1:
                    if firstCol==-1:
                        firstCol = j

                    lastCol = j

        return (lastRow-firstRow+1)*(lastCol-firstCol+1)                                


                    

        