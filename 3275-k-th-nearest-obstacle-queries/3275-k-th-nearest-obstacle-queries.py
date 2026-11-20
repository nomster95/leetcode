import heapq
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        h = []
        n = len(queries)
        ans = [0]*n

        for i in range(n):
            x = abs(queries[i][0])
            y = abs(queries[i][1])
            heapq.heappush(h,-(x+y))
            if len(h)>k:
                heapq.heappop(h)

            if len(h)<k:
                ans[i] = -1

            else:
                ans[i] = -h[0]


        return ans          
        