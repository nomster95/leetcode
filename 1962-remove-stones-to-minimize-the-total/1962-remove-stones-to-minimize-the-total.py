import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        h = []
        total = 0
        for i in piles:
            heapq.heappush(h,-i)

        for _ in range(k):
            ele = -heapq.heappop(h)
            new_ele = ele - floor(ele/2)
            heapq.heappush(h,-new_ele)


        for x in h:
            total+=abs(x)

        return total    


        
