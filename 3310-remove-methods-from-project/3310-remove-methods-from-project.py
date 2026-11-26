class Solution:
    def dfs(self,i,adjList,visited):
        visited[i] = True

        for x in adjList[i]:
            if not visited[x]:
                self.dfs(x,adjList,visited)

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        visited = [False]*n
        adjList = []
        ans = []
        for _ in range(n):
            adjList.append([])

        for u,v in invocations:
            adjList[u].append(v)

        self.dfs(k,adjList,visited)

        for u,v in invocations:
            if not visited[u] and  visited[v]:
                return [x for x in range(n)]
        

        for i in range(n):
            if not visited[i]:
                ans.append(i)


        return ans        




        