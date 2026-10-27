class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans , sol = [] , []
        n = len(graph)
        last = n-1
        def backtrack(node):
            if node==last:
                sol.append(ans[:])
                return

            for nei in graph[node]:
                ans.append(nei)
                backtrack(nei)
                ans.pop()


        ans.append(0)                  
        backtrack(0)
        return sol            

        