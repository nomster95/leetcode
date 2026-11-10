class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = {}
        count = 0
        for i in grid:
            x = tuple(i)
            if x not in freq:
                freq[x] = 1
            else:
                freq[x]+=1    
            

        # transpose:-
        rows = len(grid)
        cols = len(grid[0])
        ans = [[0]*rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                ans[j][i] = grid[i][j]
        
        
        for j in ans:
            y = tuple(j)
            if y in freq:
                count+=freq[y]

        return count        

            
        
        