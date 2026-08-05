class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        ans = 0
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if i==j or i+j==rows-1:
                    ans = ans+mat[i][j]

        
        return ans        

                  

            

        