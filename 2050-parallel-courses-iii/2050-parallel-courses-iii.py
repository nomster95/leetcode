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
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        adjList = []
        q = Queue()
        for _ in range(n+1):
            adjList.append([])

        indegree = [0]*(n+1)
        finish = [0] + time[:]

        for a,b in relations:
            indegree[b]+=1
            adjList[a].append(b)

        for i in range(1,n+1):
            if indegree[i]==0:
                q.push(i)


        while q.size()>0:
            front = q.pop()
            for x in adjList[front]:
                finish[x] = max(finish[x],finish[front]+time[x-1])
                indegree[x]-=1
                if indegree[x]==0:
                    q.push(x)

        

        return max(finish)