class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_bound = {}
        col_bound = {}
        ans = 0

        for x,y in buildings:
            if x not in row_bound:
                row_bound[x] = [y,y]
            else:
                row_bound[x][0] = min(row_bound[x][0],y)
                row_bound[x][1] = max(row_bound[x][1],y)

            if y not in col_bound:
                col_bound[y] = [x,x]
            else:
                col_bound[y][0] = min(col_bound[y][0],x)
                col_bound[y][1] = max(col_bound[y][1],x)

        for x,y in buildings:
            min_col,max_col = row_bound[x]
            min_row,max_row = col_bound[y]

            if min_row < x < max_row and min_col < y < max_col:
                ans+=1

        return ans        




                   
    
        
        