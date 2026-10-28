class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        freq = {}
        n = len(matrix)
        for i in range(len(matrix)):
            ans=""
            if matrix[i][0]==0:
                for x in matrix[i]:
                    ans+=str(x)    
            else:
                for x in matrix[i]:
                    if x==1:
                        ans+="0"
                    else:
                        ans+="1"  

            if ans not in freq:
                freq[ans] = 1
            else:
                freq[ans]+=1

        return max(freq.values())                        




            
                
                
            
        