class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        xor_sum1 = 0
        xor_sum2 = 0
        for i in arr1:
            xor_sum1^=i

        for j in arr2:
            xor_sum2^=j

        return xor_sum1&xor_sum2        
        