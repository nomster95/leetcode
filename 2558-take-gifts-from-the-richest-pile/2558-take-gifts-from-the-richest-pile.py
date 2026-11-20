import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = []
        for i in gifts:
            heapq.heappush(h,-i)

        for x in range(k):
            ele = -heapq.heappop(h)  
            new_ele = floor(sqrt(ele))
            heapq.heappush(h,-new_ele)


        return -sum(h)      
        