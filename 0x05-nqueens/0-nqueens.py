#!/usr/bin/python3
"""n queens algo"""
import sys


def print_usage():
    """helper printing"""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid(board, row, col):
    """helper validation"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, board, row, solutions):
    """solving nqueens"""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1, solutions)


def main():
    """main func"""
    if len(sys.argv) != 2:
        print_usage()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(N, board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """run main"""
    main()
