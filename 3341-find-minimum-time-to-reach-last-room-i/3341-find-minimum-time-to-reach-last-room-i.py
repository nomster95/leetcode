import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime),len(moveTime[0])
        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0,0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            t , r , c = heapq.heappop(heap)
            if t>dist[r][c]:
                continue

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<n and 0<=nc<m:
                    newTime = max(t,moveTime[nr][nc]) + 1

                    if newTime<dist[nr][nc]:
                        dist[nr][nc] = newTime
                        heapq.heappush(heap,(newTime,nr,nc))   


        return dist[n-1][m-1]                 
        