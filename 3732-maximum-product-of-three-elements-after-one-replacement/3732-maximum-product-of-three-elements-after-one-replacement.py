class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [abs(x) for x in nums]
        nums.sort()
        return nums[-1]*nums[-2]*(10**5)
        