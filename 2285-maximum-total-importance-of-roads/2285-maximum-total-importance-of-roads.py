class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        ans = 0
        degree = [0]*n
        for u,v in roads:
            degree[u]+=1
            degree[v]+=1

        degree.sort()
        for i in range(n):
            ans+=degree[i]*(i+1)

        return ans       
        