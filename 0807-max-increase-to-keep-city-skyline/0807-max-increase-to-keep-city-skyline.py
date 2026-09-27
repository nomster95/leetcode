class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        total_increase = 0
        n = len(grid)
        rowMax = []
        colMax = []
        for i in range(n):
            rowMax.append(max(grid[i]))

        for j in zip(*grid):
            colMax.append(max(j))

        for i in range(n):
            for j in range(n):
                increase = min(rowMax[i],colMax[j])-grid[i][j]
                total_increase+=increase




        return total_increase           

        