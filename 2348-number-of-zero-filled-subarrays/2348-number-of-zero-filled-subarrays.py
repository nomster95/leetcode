class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0
        n = 0
        mod = 10**9 + 7

        for i in nums:
            if i==0:
                n+=1
                count+=n
            else:
                n = 0

        return count            


        