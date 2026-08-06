class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        firstRowZero = False
        firstColZero = False

        for i in range(m):
            if matrix[0][i] ==0:
                firstRowZero = True
            

        for j in range(n):
            if matrix[j][0] ==0:
                firstColZero = True
            

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0        

        if firstRowZero:
            for i in range(m):
                matrix[0][i] = 0

        if firstColZero:
            for j in range(n):
                matrix[j][0] = 0


                        



        