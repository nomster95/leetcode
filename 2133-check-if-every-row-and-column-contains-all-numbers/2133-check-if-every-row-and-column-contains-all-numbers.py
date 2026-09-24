class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        #validate rows
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            seen = set()
            for j in range(m):
                item = matrix[i][j]
                if item in seen:
                    return False
                seen.add(item)

        #validate cols        
        for i in range(n):
            seen = set()
            for j in range(m):
                item = matrix[j][i]
                if item in seen:
                    return False
                seen.add(item)  

        return True            
        