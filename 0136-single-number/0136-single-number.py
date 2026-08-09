class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = 0
        for i in range(len(nums)):
            XOR = XOR^nums[i]

        return XOR    
        