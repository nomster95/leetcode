class Solution:
    def dfs(self,i,adjList,visited,component):
        visited[i] = True
        component.append(i)

        for x in adjList[i]:
            if not visited[x]:
                self.dfs(x,adjList,visited,component)

        
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList= []
        for i in range(n):
            adjList.append([])

        for edge in edges:
            u , v = edge

            adjList[u].append(v)
            adjList[v].append(u)

        visited = [False]*n
        ans = 0
        for i in range(n):
            if not visited[i]:
                component = []
                self.dfs(i,adjList,visited,component)

                size = len(component)
                complete = True
                for node in component:
                    if len(adjList[node])!=size-1:
                        complete = False


                if complete:
                    ans+=1


        return ans                    

        