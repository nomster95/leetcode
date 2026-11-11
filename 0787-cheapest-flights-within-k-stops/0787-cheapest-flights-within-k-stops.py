import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')]*n
        adjList = []
        for _ in range(n):
            adjList.append([])

        for edge in flights:
            x = edge[0]
            y = edge[1]
            w = edge[2]

            adjList[x].append([y,w])


        # stops,node,cost    
        heap = [[0,src,0]]  
        dist[src] = 0

        while heap:
            stops , u , d = heapq.heappop(heap)

            if stops>k:
                continue

            for v , w in adjList[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(heap,(stops+1,v,d+w))


        if dist[dst]==float('inf'):
            return -1

        return dist[dst]                

                
        