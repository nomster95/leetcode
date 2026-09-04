class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        XOR = 0
        for i in derived:
            XOR = XOR^i

        if XOR==0:
            return True
        return False        
        