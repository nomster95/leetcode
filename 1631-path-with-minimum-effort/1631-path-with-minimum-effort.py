import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m , n = len(heights) , len(heights[0])
        dist = [[float('inf')]*n for _ in range(m)]
        # diff , row ,col
        dist[0][0] = 0
        heap = [(0,0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            diff , r , c = heapq.heappop(heap)

            if diff>dist[r][c]:
                continue

            if r==m-1 and c==n-1:
                return diff    

            for dr,dc in directions:
                nr = dr + r
                nc = dc + c

                if 0<=nr<m and 0<=nc<n:
                    new_diff = max(abs(heights[r][c]-heights[nr][nc]),diff)

                    if new_diff < dist[nr][nc]:
                        dist[nr][nc] = new_diff
                        heapq.heappush(heap,(new_diff,nr,nc))

                        
                


        