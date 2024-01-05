#!/usr/bin/python3
"""Nqueens backtracking problem"""
class Nqueens:
    """class that solves Nqueens problem"""

    def __init__(self, n: int) -> list[list[str]]:
        """class that takes nxn chessboard"""

        col = set()
        pos_diag = set()
        neg_diag = set()
        result = []

        board = [["."] * n for i in range(n)]
    
        def backtrack(r):
            """backtracking algorithm"""

            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = Q

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return result

