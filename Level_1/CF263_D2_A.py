# https://codeforces.com/contest/263/problem/A

"""
Beautiful Matrix

You've got a 5x5 matrix, consisting of 24 zeroes and a single number one.
Let's index the matrix rows by numbers from 1 to 5 from top to bottom,
let's index the matrix columns by numbers from 1 to 5 from left to right.
In one move, you are allowed to apply one of the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i+1 for some integer i (1 ≤ i < 5).
Swap two neighboring matrix columns, that is, columns with indexes j and j+1 for some integer j (1 ≤ j < 5).

A matrix looks beautiful, if the single number one of the matrix is located in its middle
(in the cell that is on the intersection of the third row and the third column).

Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers:
the j-th integer in the i-th line of the input represents the element of the matrix
that is located on the intersection of the i-th row and the j-th column.
It is guaranteed that the matrix consists of 24 zeroes and a single number one.

Output
Print a single integer — the minimum number of moves needed to make the matrix beautiful.
"""

# Get 5 lines of input, check for 1 in every line, if yes:
# Line number is row number and index of '1' in the input.split() is its column number
for row_ind in range(5):
    line = input()
    if "1" in line:
        singleton_row = row_ind
        singleton_col = line.split().index("1")

# Calculate the number of moves as abs of singleton coordinates minus middle coordinates
number_of_moves = abs(singleton_row - 2) + abs(singleton_col - 2)

# Display result
print(number_of_moves)
