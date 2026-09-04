class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = [row[:] for row in board]
        n = len(board)
        m = len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]


        for i in range(n):
            for j in range(m):
                live = 0
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < n and 0 <= nj < m:
                        if matrix[ni][nj] == 1:
                            live += 1

                if matrix[i][j]==1:
                    if live<2:
                        board[i][j] = 0
                    elif live>3:
                        board[i][j] = 0
                else:
                    if live==3:
                        board[i][j] = 1






                
                
        