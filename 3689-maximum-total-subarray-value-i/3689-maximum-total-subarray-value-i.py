class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxima = max(nums)
        minima = min(nums)
        return k*(maxima-minima)