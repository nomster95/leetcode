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
    def __init__(self):
        self.adjList = []

    def bipartite(self,n,edges):
        for _ in range(n+1):
            self.adjList.append([])

        for edge in edges:
            x = edge[0]
            y = edge[1]

            self.adjList[x].append(y)
            self.adjList[y].append(x)

        V = len(self.adjList)
        color = [-1]*V

        def dfs(node,col):
            color[node] = col

            for nei in self.adjList[node]:
                if color[nei]==-1:
                    # color every neighbor with opp color
                    result = dfs(nei,1-col)
                    if result==False:
                        return False
                    
                elif color[nei] == col:
                    return False

            return True

        # for checking every component    
        for i in range(V):
            if color[i]==-1:
                if not dfs(i,0):
                    return False

        return True                       
    
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        self.adjList = []
        bipar = self.bipartite(n,edges)
        if not bipar:
            return -1

        visited = [False]*(n+1)
        components = []
        def dfs(i,visited,component):
            visited[i] = True
            component.append(i)
            for x in self.adjList[i]:
                if not visited[x]:
                    dfs(x,visited,component)

            

        for i in range(1,n+1):
            if not visited[i]:
                component = []
                dfs(i,visited,component) 
                components.append(component)  

        def bfs(start):
            q = Queue()
            q.push(start)

            visited = [False]*(n+1)
            visited[start] = True
            levels = 0

            while q.size()>0:
                level_size = q.size()

                for _ in range(level_size):
                    front = q.pop()

                    for nei in self.adjList[front]:
                        if not visited[nei]:
                            visited[nei] = True
                            q.push(nei)

                levels+=1

            return levels

        ans = 0
        for component in components:
            max_level = 0

            for node in component:
                max_level = max(max_level,bfs(node))

            ans+=max_level


        return ans        

                            




        
        
