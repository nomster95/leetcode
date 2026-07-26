
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        largest1 = nums[-1]
        largest2 = nums[-2]
        largest3 = nums[-3]
        smallest1 = nums[0]
        smallest2 = nums[1]
        return max(largest1*largest2*largest3,largest1*smallest1*smallest2)
