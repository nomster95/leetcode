class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        ans = []

        def dfs(i,adjList,visited):
            visited[i] = True
            ans.append(i)
            for x in adjList[i]:
                if not visited[x]:
                    dfs(x,adjList,visited)


        dfs(0,rooms,visited)
        return len(ans)==n            
        