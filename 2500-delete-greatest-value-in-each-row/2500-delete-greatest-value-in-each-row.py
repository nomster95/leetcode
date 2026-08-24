class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        for i in range(n):
            grid[i].sort()

        for i in zip(*grid):
            ans+=max(i)

        return ans       
        