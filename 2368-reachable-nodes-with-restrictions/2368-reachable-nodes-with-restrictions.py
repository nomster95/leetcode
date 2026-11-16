class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        seen = set(restricted)
        adjList = []
        count = set()
        visited = [False]*n
        for _ in range(n):
            adjList.append([])

        def dfs(i,adjList,visited):
            visited[i] = True
            count.add(i)

            for x in adjList[i]:
                if not visited[x]:
                    dfs(x,adjList,visited)


        for edge in edges:
            x = edge[0]
            y = edge[1]

            if x not in seen and y not in seen:
                adjList[x].append(y)
                adjList[y].append(x)

        dfs(0,adjList,visited)
        return len(count)     


        
        