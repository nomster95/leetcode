class Solution:
    def maxDistinct(self, s: str) -> int:
        a = set()
        for i in s:
            a.add(i)
            
        return len(a)