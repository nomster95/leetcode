class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d  = 1
        i = 0

        grid = [[] for _ in range(numRows)]
        if numRows==1:
            return s

        for ch in s:
            grid[i].append(ch)
            if i==0:
                d = 1
            elif i==numRows-1:
                d = -1
            i+=d

        ans = ""
        for i in range(numRows):
            ans+= "".join(grid[i])

        return ans            

                
        
        
        

        