# 0x05. N Queens
# N Queens Problem Solver

The N queens problem is a classic problem in the field of computer science and mathematics. The challenge is to place N non-attacking queens on an N×N chessboard. A queen can attack horizontally, vertically, and diagonally.

This Python program provides a solution to the N queens problem using backtracking. It generates and prints all possible solutions for a given N.

## Usage:
```
    ...$ nqueens N
```

- If the user calls the program with the wrong number of arguments, it prints `Usage: nqueens N` and exits with the status 1.
- N must be an integer greater than or equal to 4.
- If N is not an integer, it prints `N must be a number` and exits with the status 1.
- If N is smaller than 4, it prints `N must be at least 4` and exits with the status 1.

The program prints every possible solution to the problem, one solution per line.

## Example

To solve the N queens problem for N = 4:

```
    $ ./nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
```


## How it Works
```
    The program uses backtracking to recursively place queens
    on the chessboard, ensuring that no two queens attack each other.
    Backtracking is a depth-first search algorithm that explores all
    possible solutions by incrementally building up a solution and
    backtracking when it reaches a dead-end. 
```
1. **is_safe Function**: Checks if it's safe to place a queen at a given position on the chessboard. It ensures that no other queen attacks the current position.

2. **solve_nqueens_util Function**: A recursive utility function to solve the N Queens problem. It tries to place a queen in each column of the current row and recursively moves to the next row.

3. **solve_nqueens Function**: The main function to solve the N Queens problem. It initializes the chessboard, calls the solve_nqueens_util function, and prints all solutions found.

## Queen
```
    In chess, a queen can move any number of 
    squares vertically, horizontally, or diagonally.
    In the N queens problem,
    we are placing N queens on an N×N chessboard
    such that no two queens threaten each other.
```
## Backtracking
```
    Backtracking is a general algorithm for finding all (or some) solutions to some computational problems,
    notably constraint satisfaction problems.
    It incrementally builds candidates to the solutions,
    and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
```

## File Structure
- `0-nqueens.py`: The Python script containing the solution.
- `README.md`: This README file.

## Requirements
- Python 3.x