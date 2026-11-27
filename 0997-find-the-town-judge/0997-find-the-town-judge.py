class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        indegree = [0]*(n)
        outdegree = [0]*(n)

        for a,b in trust:
            indegree[b-1]+=1
            outdegree[a-1]+=1

        for i in range(n):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i+1

        return -1        


        