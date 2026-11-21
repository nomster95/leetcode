import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        h = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(h,(nums[i],i))

        seen = set()
        while h:
            ele,i = heapq.heappop(h)  
            if i not in seen:
                score+=ele
                seen.add(i)
                if i+1<n and i+1 not in seen:
                    seen.add(i+1)
                if i-1>=0 and i-1 not in seen:
                    seen.add(i-1)

        return score                

        
        