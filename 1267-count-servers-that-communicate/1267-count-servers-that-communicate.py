class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        servers = 0
        m,n = len(grid),len(grid[0])
        rowcount = []
        colcount = []
        isolated = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    servers+=1
                    row_server = False
                    col_server = False
                    for c  in range(n):
                        if c!=j and grid[i][c]==1:
                            row_server = True

                    for r in range(m):
                        if r!=i and grid[r][j]==1:
                            col_server  = True

                    if not row_server and not col_server:
                        isolated+=1


        return servers-isolated                

                    


        