class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        V = len(graph)
        color = [-1]*V

        def dfs(node,col):
            color[node] = col

            for nei in graph[node]:
                if color[nei]==-1:
                    if not dfs(nei,1-col):
                        return False
                elif color[nei] == col:
                    return False

            return True

        for i in range(V):
            if color[i]==-1:
                if not dfs(i,0):
                    return False

        return True                                

        