class Solution:
    def minOperations(self, s: str) -> int:
        ops = []
        for i in s:
            trans = (26 - (ord(i)-ord('a')))%26
            ops.append(trans)

        return max(ops)    
        