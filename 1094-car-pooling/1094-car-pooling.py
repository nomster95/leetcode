import heapq
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        h = []
        currPass = 0
        for t in trips:
            numPass , start ,  end = t
            while h and h[0][0]<=start:
                currPass-=h[0][1]
                heapq.heappop(h)

            currPass+=numPass
            if currPass>capacity:
                return False

            heapq.heappush(h,[end,numPass])

        return True            
        