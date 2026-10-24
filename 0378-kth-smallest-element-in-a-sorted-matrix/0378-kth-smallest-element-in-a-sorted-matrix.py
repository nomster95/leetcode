
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                h.append(matrix[i][j])


        h.sort()
        return h[k-1]        
                