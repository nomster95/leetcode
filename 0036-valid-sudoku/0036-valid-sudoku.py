class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #validate rows
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[i][j]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)

        #validate cols        
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[j][i]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)  

        #validate boxes
        #get the starting point of each box
        starts = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)]

        for i, j in starts:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)

        return True
        #TIME = O(1)
        #space = O(1)                    

        