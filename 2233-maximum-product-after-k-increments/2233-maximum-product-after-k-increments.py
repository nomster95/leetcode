import heapq
class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        h = []
        ans = 1
        for i in nums:
            heapq.heappush(h,i)

        for _ in range(k):
            ele = heapq.heappop(h)
            heapq.heappush(h,ele+1)

        for x in h:
            ans = (ans*x)%mod

        return ans%mod    

        