import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        dist = [[float('inf')]*n for _ in range(m)]
        # val , row ,col
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0],0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            val , r , c = heapq.heappop(heap)

            if val>dist[r][c]:
                continue

            if r==m-1 and c==n-1:
                return val    

            for dr,dc in directions:
                nr = dr + r
                nc = dc + c

                if 0<=nr<m and 0<=nc<n:
                    new_val = max(grid[nr][nc],val)

                    if new_val < dist[nr][nc]:
                        dist[nr][nc] = new_val
                        heapq.heappush(heap,(new_val,nr,nc))

        