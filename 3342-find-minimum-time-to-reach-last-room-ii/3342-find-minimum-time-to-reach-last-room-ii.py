class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime),len(moveTime[0])
        dist = [[[float('inf')]*2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0
        heap = [(0,0,0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        move = 0

        while heap:
            t , r , c , move = heapq.heappop(heap)
            cost = 1 if move==0 else 2
            next_move = 1-move
            if t>dist[r][c][move]:
                continue


            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                

                if 0<=nr<n and 0<=nc<m:
                    newTime = max(t,moveTime[nr][nc])+cost
             

                    if newTime<dist[nr][nc][next_move]:
                        dist[nr][nc][next_move] = newTime
                        heapq.heappush(heap,(newTime,nr,nc,next_move))             

             


        return min(dist[n-1][m-1][0],dist[n-1][m-1][1])               
        
        