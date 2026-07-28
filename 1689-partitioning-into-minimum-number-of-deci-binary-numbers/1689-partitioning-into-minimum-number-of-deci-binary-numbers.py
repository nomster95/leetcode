class Solution:
    def minPartitions(self, n: str) -> int:
        s = []
        for i in n:
            s.append(int(i))
        
        return max(s)