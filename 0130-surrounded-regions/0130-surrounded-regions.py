class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])
        st = []
        # first apply dfs on the edges
        # first and last rows:
        for j in range(n):
            if board[0][j]=="O":
                st.append((0,j))

            if m>1 and board[m-1][j]=="O":
                st.append((m-1,j))

        # first and last col:     
        for i in range(1,m-1):
            if board[i][0]=="O":
                st.append((i,0))

            if n>1 and board[i][n-1]=="O":
                st.append((i,n-1))  

        while st:
            i , j = st.pop()
            board[i][j] = "S"
            for i_off,j_off in [(-1,0),(0,1),(1,0),(0,-1)]:
                r , c = i + i_off , j+ j_off
                if 0<=r<m and 0<=c<n and board[r][c]=="O":
                    st.append((r,c))       


        # change all s to o and o to x:
        for i in range(m):
            for j in range(n):
                if board[i][j]=="S":
                    board[i][j] = "O"
                elif board[i][j]=="O":
                    board[i][j] = "X"










        