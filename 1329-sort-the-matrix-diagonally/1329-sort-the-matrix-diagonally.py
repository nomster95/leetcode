class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])      
        for col_start in range(1,m):
            i = 0
            j = col_start
            ans = []
            while i<n and j<m:
                ans.append(mat[i][j])
                
                i+=1
                j+=1
            ans.sort()
            i = 0
            j = col_start
            k = 0
            while i<n and j<m:
                mat[i][j] = ans[k]
                i+=1
                j+=1
                k+=1



        for row_start in range(n):
            i = row_start
            j=0
            ans = []
            while i<n and j<m:
                ans.append(mat[i][j]) 
                 
                i+=1
                j+=1     
            ans.sort() 
            i = row_start
            j = 0
            k = 0
            while i<n and j<m:
                mat[i][j] = ans[k]
                i+=1
                j+=1
                k+=1

        return mat       


        