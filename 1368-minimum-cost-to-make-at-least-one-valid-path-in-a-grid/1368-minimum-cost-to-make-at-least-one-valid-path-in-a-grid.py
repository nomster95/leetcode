import heapq
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        h = [(0,0,0)]
        directions = [(1, 0, 3),   # Down
                    (-1, 0, 4),  # Up
                    (0, 1, 1),   # Right
                     (0, -1, 2) ]  # Left

        while h:
            cost,r,c = heapq.heappop(h)
            if cost>dist[r][c]:
                continue

            for dr,dc,direction in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<m and 0<=nc<n:
                    if grid[r][c]==direction:
                        new_cost = cost
                    else:
                        new_cost = cost+1


                    if new_cost<dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(h,(new_cost,nr,nc))



        return dist[m-1][n-1]                                     


        