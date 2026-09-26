class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solution = []
        used_cols = set()
        used_pos_diags = set() # row+col
        used_neg_diags = set() #row-col
        queen_col_indices = []
        def backtrack(row):
            #base case
            if row==n:
                board = []
                for c in queen_col_indices:
                    dots_before = '.'*c
                    dots_after = '.'*(n-c-1)
                    row_string = dots_before + 'Q' + dots_after
                    board.append(row_string)
                solution.append(board)

            for col in range(n):
                if col in used_cols or (row+col) in used_pos_diags or (row-col) in used_neg_diags:
                    continue

                queen_col_indices.append(col)
                used_cols.add(col)
                used_pos_diags.add(row+col)
                used_neg_diags.add(row-col)

                backtrack(row+1)

                queen_col_indices.pop()
                used_cols.remove(col)
                used_pos_diags.remove(row+col)
                used_neg_diags.remove(row-col)

        backtrack(0)
        return solution        



        