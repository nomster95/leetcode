class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        XOR = 0
        for i in nums:
            XOR = XOR^i

        return XOR    
        