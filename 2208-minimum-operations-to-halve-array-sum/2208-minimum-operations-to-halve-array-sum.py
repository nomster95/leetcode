import heapq
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        h = []
        for i in nums:
            heapq.heappush(h,-i)

        total = 0
        limit = sum(nums)/2

        ops = 0
        while total<limit:
            ele = -heapq.heappop(h)   
            new_ele = ele/2
            reduction = ele - new_ele

            total+=reduction
            heapq.heappush(h,-new_ele)

            ops+=1

        return ops    


        