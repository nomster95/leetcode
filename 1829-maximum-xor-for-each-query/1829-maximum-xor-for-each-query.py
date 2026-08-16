class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        XOR = 0
        for i in nums:
            XOR = XOR^i

        for i in range(len(nums)-1,-1,-1):
            k  = ((2**maximumBit) - 1) ^ XOR  
            answer.append(k)
            XOR = XOR^nums[i]

        return answer    


        