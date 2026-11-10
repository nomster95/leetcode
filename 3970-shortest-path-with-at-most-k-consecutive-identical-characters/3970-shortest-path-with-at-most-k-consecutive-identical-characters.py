import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adjList = []
        for i in range(n):
            adjList.append([])
        for edge in edges:
            x = edge[0]
            y = edge[1]
            w = edge[2]

            adjList[x].append([y,w])

        dist = [[float('inf')]*(k+1) for _ in range(n)]
        heap = []
        dist[0][1] = 0
        heap = [(0,0,1)]    

        while heap:
            d , u , count= heapq.heappop(heap)
            if d>dist[u][count]:
                continue
 

            for v , w in adjList[u]:
                new_count = 1
                if labels[u]==labels[v]:
                    new_count = count + 1 

                if new_count>k:
                    continue

                if d + w < dist[v][new_count]:
                    dist[v][new_count] = d + w
                    heapq.heappush(heap,(d+w,v,new_count))    


        ans = min(dist[n-1][1:])
        if ans==float('inf'):
            return -1

        return ans                        


        