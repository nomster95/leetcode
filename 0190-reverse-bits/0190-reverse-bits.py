class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            bit = n&1
            ans = ans<<1
            ans = ans | bit
            n = n>>1

        return ans    


        