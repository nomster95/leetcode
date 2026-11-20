import heapq
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        h = [-a,-b,-c]
        heapq.heapify(h)
        ops = 0
        while len(h)>1:
            ops+=1
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            if x+1!=0:
                heapq.heappush(h,x+1)

            if y+1!=0:    
                heapq.heappush(h,y+1)

        return ops        





        