import heapq
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = [0]*n
        h = []
        seen = set()
        total = sum(nums)
        for i in range(len(nums)):
            heapq.heappush(h,(nums[i],i))

        for i in range(n):
            ind,k = queries[i]
            if ind not in seen:
                seen.add(ind)
                total-=nums[ind]
            x = 0
            while x<k and h:
                index = heapq.heappop(h)[1]
                if index not in seen:
                    seen.add(index)
                    total-=nums[index]
                    x+=1


            ans[i] = total

        return ans                    
                



        