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
    def checkIfPrerequisite(self, n: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        q = Queue()
        ans = []
        indegree = [0]*n
        pre = [set() for _ in range(n)]
        adjList = []
        sol = [True]*len(queries)
        for _ in range(n):
            adjList.append([])

        for a,b in prerequisites:
            #a->b
            indegree[b]+=1
            adjList[a].append(b)

        for i in range(n):
            if indegree[i]==0:
                ans.append(i)
                q.push(i)


        while q.size()>0:
            front = q.pop()
            for x in adjList[front]:
                pre[x].add(front)
                pre[x].update(pre[front])     
                indegree[x]-=1

                if indegree[x]==0:
                    ans.append(x)
                    q.push(x)

        for i in range(len(queries)):
            if queries[i][0] not in pre[queries[i][1]]:
                sol[i] = False

        return sol        



    


        