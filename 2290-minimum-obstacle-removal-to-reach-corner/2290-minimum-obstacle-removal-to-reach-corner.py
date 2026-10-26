import heapq
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m , n = len(grid),len(grid[0])
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0,0,0)] # weight,row,col

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            d,r,c = heapq.heappop(heap)

            if d>dist[r][c]:
                continue

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<m and 0<=nc<n:
                    new_cost = d + grid[nr][nc]   

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(heap,(new_cost,nr,nc))

        return dist[m-1][n-1]                 
        