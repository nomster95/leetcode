import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.seen = set()
        self.next_num = 1
        

    def popSmallest(self) -> int:
        if self.heap:
            ans = heapq.heappop(self.heap)
            self.seen.remove(ans)
            return ans
        else:
            ans = self.next_num
            self.next_num+=1
            return ans    

        
        

    def addBack(self, num: int) -> None:
        if num<self.next_num and num not in self.seen:
            heapq.heappush(self.heap,num)
            self.seen.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)