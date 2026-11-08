import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [float('inf')]*n
        
        heap = []
        adjList = []
        for _ in range(n):
            adjList.append([])
        for edge in edges:
            x = edge[0]
            y = edge[1]
            w = edge[2]

            adjList[x].append([y,w])
            adjList[y].append([x,2*w])

        s = 0
        dist[s] = 0
        heapq.heappush(heap,(dist[s],s))

        while heap:
            d , u = heapq.heappop(heap)
            if d>dist[u]:
                continue

            for v,w in adjList[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(heap,(dist[v],v))


        if dist[n-1]==float('inf'):
            return -1

        return dist[n-1]                   


        