class Solution:
    def numEnclaves(self, board: list[list[int]]) -> int:
        m = len(board)
        n = len(board[0])
        st = []
        enclaves = 0
        # dfs using stack
        # first apply dfs on the edges
        # first and last rows:
        for j in range(n):
            if board[0][j]==1:
                st.append((0,j))

            if m>1 and board[m-1][j]==1:
                st.append((m-1,j))

        # first and last col:     
        for i in range(1,m-1):
            if board[i][0]==1:
                st.append((i,0))

            if n>1 and board[i][n-1]==1:
                st.append((i,n-1))  

        while st:
            i , j = st.pop()
            board[i][j] = 2
            for i_off,j_off in [(-1,0),(0,1),(1,0),(0,-1)]:
                r , c = i + i_off , j+ j_off
                if 0<=r<m and 0<=c<n and board[r][c]==1:
                    st.append((r,c))       


        # change all s to o and o to x:
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    enclaves+=1

        return enclaves            
                