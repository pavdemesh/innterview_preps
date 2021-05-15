# https://codeforces.com/contest/298/problem/A

"""
Snow Footprints

There is a straight snowy road, divided into n blocks. The blocks are numbered from 1 to n from left to right.
If one moves from the i-th block to the (i+1)-th block, he will leave a right footprint on the i-th block.
Similarly, if one moves from the i-th block to the (i-1)-th block, he will leave a left footprint on the i-th block.
If there already is a footprint on the i-th block, the new footprint will cover the old one.

At the beginning, there were no footprints.
Then polar bear Alice starts from the s-th block, makes a sequence of moves and ends in the t-th block.
It is known that Alice never moves outside of the road.

You are given the description of Alice's footprints.
Your task is to find a pair of possible values of s, t by looking at the footprints.

Input
The first line of the input contains integer n (3 <= n <= 1000).
The second line contains the description of the road — the string that consists of n characters.
Each character will be either "." (a block without footprint),
or "L" (a block with a left footprint), "R" (a block with a right footprint).
It's guaranteed that the given string contains at least one character not equal to ".".
Also, the first and the last character will always be ".". It's guaranteed that a solution exists.

Output
Print two space-separated integers — the values of s and t.
If there are several possible solutions you can print any of them.

Input:
9
..RRLL...

Output:
3 4
"""

# Get input n - size of the road
n = int(input())
# Get the road formula, convert to a list and add "." at the beginning to account for numbering starting at 1.
road = ["."] + list(input())

# Set starting and ending points to None
start_point = None
end_point = None

# Consider 4 possible scenarios

# If "L" not in road: the journey will start at first R and end after count(R) steps
if "L" not in road:
    start_point = road.index("R")
    end_point = start_point + road.count("R")
# Else the journey can start at "L" and end at index("L") - 1
else:
    start_point = road.index("L")
    end_point = start_point - 1

print(start_point, end_point)
