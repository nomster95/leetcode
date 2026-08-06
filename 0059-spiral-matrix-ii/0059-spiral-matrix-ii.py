class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0]*n for _ in range(n)]
        
        
        ans = 1
        
        total = n*n
        rowstart = 0
        colstart = 0
        rowend = n-1
        colend = n-1
        while ans<=total:
            #rowstart, colstart-colend:
            for i in range(colstart,colend+1):
                matrix[rowstart][i] = ans
                ans+=1
            rowstart+=1
            
            #colend,rowstart-rowend:
            for i in range(rowstart,rowend+1):
                matrix[i][colend] = ans
                ans+=1
            colend-=1
            

            #rowend,colend-colstart:
            for i in range(colend,colstart-1,-1):
                matrix[rowend][i] = ans
                ans+=1

            rowend-=1  
            

            #colstart,rowend-rowstart:
            for i in range(rowend,rowstart-1,-1):
                matrix[i][colstart] = ans
                ans+=1
            colstart+=1

        return matrix       

        
        