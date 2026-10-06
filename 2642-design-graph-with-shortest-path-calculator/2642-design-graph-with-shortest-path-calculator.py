import heapq
class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adjList = []
        for i in range(n):
            self.adjList.append([])

        for edge in edges:
            u,v,w = edge
            self.adjList[u].append([v,w])
        

    def addEdge(self, edge: list[int]) -> None:
        u,v,w = edge
        self.adjList[u].append([v,w])


        

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adjList)
        heap = []
        dist = [float('inf')]*n
        dist[node1] = 0
        heapq.heappush(heap,(0,node1))

        while len(heap)>0:
            d,u = heapq.heappop(heap)
            for v,w in self.adjList[u]:
                if d + w < dist[v]:
                    dist[v] = d+w
                    heapq.heappush(heap,(dist[v],v))

        if dist[node2]==float('inf'):
            return -1

        return dist[node2]


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)