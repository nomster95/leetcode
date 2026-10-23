class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        par = [i for i in range(N+1)] # ith node -> 1-n parent
        rank = [1]*(N+1)

        def find(n):
            if n!=par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return False

            if rank[p1]<rank[p2]:
                p1,p2 = p2,p1
                

            par[p2] = p1
            rank[p1]+=rank[p2]

            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]



        