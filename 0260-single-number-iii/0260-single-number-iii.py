class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        XOR = 0
        for i in range(len(nums)):
            XOR = XOR^nums[i]

        rightmost = XOR & -XOR
        b1 = 0
        b2 = 0
        for i in range(len(nums)):
            if nums[i]&rightmost!=0:
                b1 = b1^nums[i]
            else:
                b2 = b2^nums[i]

        return [b1,b2]                
        