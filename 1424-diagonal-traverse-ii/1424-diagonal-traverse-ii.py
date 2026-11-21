class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        freq = {}
        m = len(mat)
        n = len(mat[0])
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j not in freq:
                    freq[i+j] = [mat[i][j]]
                else:
                    freq[i+j].append(mat[i][j])

        for i in freq:
                ans+=freq[i][::-1]
            

        return ans    

        