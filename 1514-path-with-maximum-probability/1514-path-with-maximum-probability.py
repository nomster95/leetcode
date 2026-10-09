import heapq
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        adjList = []
        for i in range(n):
            adjList.append([])

        for i,edge in enumerate(edges):
            u , v = edge
            p = succProb[i]

            adjList[u].append([v,p])
            adjList[v].append([u,p])

        heap = []
        prob = [0.0]*n
        prob[start] = 1.0
        heapq.heappush(heap,(-1.0,start))

        while heap:
            neg_p , u = heapq.heappop(heap)
            p = -neg_p
            if p<prob[u]:
                continue

            if u==end:
                return p

            for v,w in adjList[u]:
                new_p = p*w

                if new_p>prob[v]:
                    prob[v] = new_p
                    heapq.heappush(heap,(-prob[v],v))     


        return prob[end]               
            



        