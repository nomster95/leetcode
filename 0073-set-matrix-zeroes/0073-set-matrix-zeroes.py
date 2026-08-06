class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)

        for i in range(n):
            for j in range(m): 
                if i in rows or j in cols:
                    matrix[i][j] = 0

