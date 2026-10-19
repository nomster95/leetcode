class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        
        final = []
        for i in range(n):
            arr = grid[i]
            arr.sort(reverse=True)
            for j in range(limits[i]):
                final.append(arr[j])

        final.sort(reverse=True)
        return sum(final[:k])


        