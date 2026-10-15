class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        s = (2*k)+1
        return ceil(n/s)*ceil(m/s)
        