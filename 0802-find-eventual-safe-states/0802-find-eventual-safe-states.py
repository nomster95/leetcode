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
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        adjList = []
        ans = []
        q = Queue()
        for i in range(n):
            adjList.append([])

        indegree = [0]*n

        for i in range(n):
            for x in graph[i]:
                # original : i->x
                # reversed : x->i
                adjList[x].append(i)
                indegree[i]+=1

        for i in range(n):
            if indegree[i]==0:
                ans.append(i)
                q.push(i)    

        while q.size()>0:
            front = q.pop()
            for x in adjList[front]:
                indegree[x]-=1
                if indegree[x]==0:
                    ans.append(x)
                    q.push(x)


        return sorted(ans)                            





        