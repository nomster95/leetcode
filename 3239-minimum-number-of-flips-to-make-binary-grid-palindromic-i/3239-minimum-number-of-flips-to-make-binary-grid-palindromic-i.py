class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        row_flips = 0
        col_flips = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m//2):
                if grid[i][j]!=grid[i][m-1-j]:
                    row_flips+=1

        for i in range(n//2):
            for j in range(m):
                if grid[i][j]!=grid[n-i-1][j]:
                    col_flips+=1            



        return min(row_flips,col_flips)               
        