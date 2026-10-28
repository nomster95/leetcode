class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        ans = []
        indegree = [0]*n
        for u,v in edges:
            indegree[v]+=1

        for i in range(n):
            if indegree[i]==0:
                ans.append(i)

        return ans            


            

                  

        