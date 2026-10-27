class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        mat = [["#"]*n for _ in range(m)]
        for i in range(n):
            mat[0][i] = "."

        for j in range(1,m):
            mat[j][n-1] = "."

        ans = []
        for i in mat:
            x = "".join(i)  
            ans.append(x)

        return ans        
        