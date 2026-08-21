class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        dist = 0
        while ans!=0:
            dist+= ans&1

            ans = ans>>1

        return dist    

        