import heapq
class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        score = 0
        h = []
        for i in nums:
            heapq.heappush(h,-i)

        for x in range(k):
            ele = -heapq.heappop(h)
            score+=ele
            new_ele = ceil(ele/3)
            heapq.heappush(h,-new_ele)

        return score    


        