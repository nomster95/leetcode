class Solution:
    def dfs(self,i,visited,adjList):
        visited[i] = True
        for x in adjList[i]:
            if not visited[x]:
                self.dfs(x,visited,adjList)
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        count = 0
        if n-1>len(connections):
            return -1

        visited = [False]*(n)    

        adjList = []
        for _ in range(n):
            adjList.append([])

        for edge in connections:
            x,y = edge[0],edge[1]
            adjList[x].append(y)
            adjList[y].append(x)


        for i in range(n):
            if not visited[i]:
                self.dfs(i,visited,adjList)
                count+=1


        return count -1        







        