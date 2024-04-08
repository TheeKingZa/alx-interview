#!/usr/bin/env python3

"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
This program solves the N queens problem and prints every possible solution to the problem.
"""

import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position on the board.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N):
    """
    Solve the N queens problem and print every possible solution.
    """
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        pass

def solve_nqueens_util(board, row, N):
    """
    Helper function to recursively solve the N queens problem.
    """
    if row >= N:
        print_board(board)
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_nqueens_util(board, row + 1, N):
                pass
            board[row][col] = 0
    
    return False

def print_board(board):
    """
    Print the current state of the board.
    """
    solutions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                solutions.append([i, j])
    print(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
