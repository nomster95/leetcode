class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x = max(nums)
        ans = 0
        for i in nums:
            if i<x:
                ans+=(x-i)

        return ans        
        