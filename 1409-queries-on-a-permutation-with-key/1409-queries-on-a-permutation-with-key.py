class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [x for x in range(1,m+1)]
        ans = [0]*len(queries)

        for i in range(len(queries)):
            ans[i] = P.index(queries[i])
            P.remove(queries[i])
            P = [queries[i]]+P

        return ans    


        