import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        h = []
        for i in nums:
            heapq.heappush(h,i)

        while len(h)>1 and h[0]<k:
            ops+=1
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            new_ele = (min(x,y)*2)+max(x,y)
            
            heapq.heappush(h,new_ele)

        return ops        


        