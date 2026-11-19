from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        n = len(nums)
        ans = []

        for i in range(n):
            if dq and dq[0]<=i-k:
                dq.popleft()

            while dq and nums[dq[-1]]<=nums[i]: #monotonic deque
                dq.pop()

            dq.append(i) 

            if i>=k-1:
                ans.append(nums[dq[0]])

        return ans                    
        