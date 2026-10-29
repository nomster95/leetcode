class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ans = []
        indegree = [0]*n
        for u,v in edges:
            indegree[v]+=1

        for i in range(n):
            if indegree[i]==0:
                ans.append(i)

        if len(ans)==1:
            return ans[0]
        else:
            return -1               

        