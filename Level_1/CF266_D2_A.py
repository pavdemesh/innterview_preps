# https://codeforces.com/contest/266/problem/A

"""
Stones on the Table

There are n stones on the table in a row, each of them can be red, green or blue.
Count the minimum number of stones to take from the table so that any two neighboring stones had different colors.
Stones in a row are considered neighboring if there are no other stones between them.

Input
The first line contains integer n (1 <= n <= 50) — the number of stones on the table.
The next line contains string s, which represents the colors of the stones.
We'll consider the stones in the row numbered from 1 to n from left to right.
Then the i-th character s equals "R", if the i-th stone is red, "G", if it's green and "B", if it's blue.

Output
Print a single integer — the answer to the problem.

Examples
input
3
RRG
output
1
"""

# Get input
total_stones = int(input()) # actually,not not needed for solution in Python (replaceable by len())
color_scheme = input()

# Initialize current index to 0 and next index to 1
curr_ind = 0
next_ind = 1

# Initialize counter for items to be removed
counter_to_remove = 0

# Iterate over the colors while next index is within the length of the color scheme
while next_ind < len(color_scheme):
    # if current and next (neighboring) colors are the same: increase counter for stones to be removed and update next.
    if color_scheme[curr_ind] == color_scheme[next_ind]:
        counter_to_remove += 1
        next_ind += 1
    # Else (if neighboring colors are different), update both current and next indices
    else:
        curr_ind = next_ind
        next_ind += 1

print(counter_to_remove)
