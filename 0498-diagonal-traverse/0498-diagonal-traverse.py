class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        freq = {}
        m = len(mat)
        n = len(mat[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if i+j not in freq:
                    freq[i+j] = [mat[i][j]]
                else:
                    freq[i+j].append(mat[i][j])

        for i in freq:
            if i%2==0:
                new_arr = freq[i][::-1]
                ans+=new_arr
            else:
                ans+=freq[i]    
            

        return ans    

        