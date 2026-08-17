class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        XOR = 0
        for i in range(n):
            XOR = XOR^(start + 2*i)

        return XOR    

        