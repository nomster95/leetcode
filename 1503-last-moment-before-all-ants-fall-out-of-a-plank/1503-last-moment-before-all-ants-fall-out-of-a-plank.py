class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        if len(left)==0:
            return n-min(right)

        if len(right)==0:
            return max(left)    

        return max(max(left),n-min(right))