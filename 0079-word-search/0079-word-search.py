class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board) 
        m = len(board[0])
        w = len(word)
        if n==1 and m==1:
            return board[0][0]==word

        def backtrack(pos,index):
            i , j = pos
            
            if index==w:
                return True

            if board[i][j] != word[index]:
                return False

            char = board[i][j]
            board[i][j] = "#"     
            for i_off,j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                r ,c = i + i_off , j + j_off
                if 0 <= r < n and 0<= c < m:
                    if backtrack((r,c),index+1):
                        return True

            board[i][j] = char
            return False

        for i in range(n):
            for j in range(m):
                if backtrack((i,j),0):
                    return True

        return False                             

