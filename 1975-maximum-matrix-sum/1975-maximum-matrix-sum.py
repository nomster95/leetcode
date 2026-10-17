class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        abs_sum = 0
        negative = 0
        min_val = float('inf')
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]<0:
                    negative+=1
                abs_sum+=abs(matrix[i][j])
                min_val = min(min_val,abs(matrix[i][j]))

        if negative%2==0:
            return abs_sum
        else:
            return abs_sum - 2*min_val            



        