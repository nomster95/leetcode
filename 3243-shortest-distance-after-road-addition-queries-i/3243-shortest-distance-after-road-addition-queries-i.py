class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self,x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)  
    def pop(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front+=1
        if(self.front == len(self.q)):
            self.front = -1
            self.q = []  
        return x
    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]     
    def size(self):
        if len(self.q) == 0:
            return 0
        return len(self.q) - self.front    
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(adjList,n):
            q = Queue()
            dist = [-1]*n
            dist[0] = 0
            q.push(0)

            while q.size()>0:
                u = q.pop()
                for v in adjList[u]:
                    if dist[v]==-1:
                        dist[v] = dist[u]+1
                        q.push(v)

            return dist[n-1]

        adjList = []
        sol = []
        for _ in range(n):
            adjList.append([])

        for i in range(n-1):
            adjList[i].append(i+1)

        for x,y in queries:
            adjList[x].append(y)
            ans = bfs(adjList,n)
            sol.append(ans)

        return sol        




        