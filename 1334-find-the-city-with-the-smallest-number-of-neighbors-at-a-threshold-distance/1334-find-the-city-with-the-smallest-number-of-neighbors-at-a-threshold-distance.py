class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        #dijkstra algorithm
        adjList = []

        for i in range(n):
            adjList.append([])

        for edge in edges:
            x = edge[0]
            y = edge[1]
            w = edge[2]

            adjList[x].append([y,w])
            adjList[y].append([x,w])

        ans = -1
        min_count = float('inf')    

        for src in range(n):  
            count = -1
            heap = []
            dist = [float('inf')]*n
            
            dist[src] = 0
            heapq.heappush(heap,(dist[src],src))

            while len(heap)>0:
                d,u = heapq.heappop(heap)
                for v,w in adjList[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(heap,(dist[v],v))

            for d in dist:
                if d<=distanceThreshold:
                    count+=1

            if count<=min_count:
                min_count = count
                ans = src


        return ans               


           
        