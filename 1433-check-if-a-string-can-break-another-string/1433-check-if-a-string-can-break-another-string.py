class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        lst1 = list(s1)
        lst2 = list(s2)
        lst1.sort()
        lst2.sort()
        is_break1 = True
        is_break2 = True
        for i in range(len(s1)):
            if lst1[i]<lst2[i]:
                is_break1 = False
            
            if lst2[i]<lst1[i]:
                is_break2 = False

        return is_break1 or is_break2        

            