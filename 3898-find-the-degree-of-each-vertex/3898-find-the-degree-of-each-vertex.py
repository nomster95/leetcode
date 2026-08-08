class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for i in matrix:
            ans.append(sum(i))

        return ans    
        