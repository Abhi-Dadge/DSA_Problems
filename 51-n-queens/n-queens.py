class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."]* n for _ in range(n)]
        cols = set()
        dig1 = set()
        dig2 = set()

        def backtrack(row):
            if row == n:
                temp = []
                for r in board:
                    temp.append("".join(r))
                res.append(temp)
                return 
            for col in range(n):
                if col in cols or (row-col) in dig1 or(row+col)in dig2:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                dig1.add(row-col)
                dig2.add(row+col)

                backtrack(row+1)

                board[row][col]="."
                cols.remove(col)
                dig1.remove(row-col)
                dig2.remove(row+col)
        backtrack(0)
        return res