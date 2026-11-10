import heapq
class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        # 4D dijkstra (skull emoji)
        m , n = len(grid) , len(grid[0])
        if m==1 and n==1:
            return grid[0][0]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        dist = [[[[float('inf')]*(k+1) for _ in range(5)] for _ in range(n)] for _ in range(m)]
        # row,col,prev_direction,k,value at that grid
        # 4 rep the initial state, no prev direc
        dist[0][0][4][0] = grid[0][0]
        # cost,row,col,turns(k),prev_directions
        heap = [(grid[0][0],0,0,0,4)]

        while heap:
            cost , r , c , turns , prev_dir = heapq.heappop(heap)

            if cost > dist[r][c][prev_dir][turns]:
                continue

            for new_dir,(dr,dc) in enumerate(directions):
                nr = r + dr
                nc = c + dc
                new_turns = turns

                if 0<=nr<m and 0<=nc<n:
                    if prev_dir!=4 and new_dir!=prev_dir:
                        new_turns+=1

                    if new_turns>k:
                        continue

                    
                    new_cost = cost + grid[nr][nc]
                    if new_cost<dist[nr][nc][new_dir][new_turns]:
                        dist[nr][nc][new_dir][new_turns] = new_cost
                        heapq.heappush(heap,(new_cost,nr,nc,new_turns,new_dir))

        ans = float('inf')
        for d in range(4):
            for t in range(k+1):
                ans = min(ans,dist[m-1][n-1][d][t])                        




        if ans==float('inf'):
            return -1

        return ans    