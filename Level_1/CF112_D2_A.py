# https://codeforces.com/contest/112/problem/A

"""
Petya and Strings

Little Petya loves presents. His mom bought him two strings of the same size for his birthday.
The strings consist of uppercase and lowercase Latin letters.
Now Petya wants to compare those two strings lexicographically.
The letters' case does not matter.
An uppercase letter is considered equivalent to the corresponding lowercase letter.
Help Petya perform the comparison.

Input:
Each of the first two lines contains a bought string.
The strings' lengths range from 1 to 100 inclusive.
It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output:
If the first string is less than the second one, print "-1".
If the second string is less than the first one, print "1".
If the strings are equal, print "0".
Note that the letters' case is not taken into consideration when the strings are compared.

Example input:
aaaa
aaaA
Example output:
0
"""

# Get input
line1 = input()
line2 = input()

# Create flag for string equality
strings_are_equal = True

# Set starting index for iteration to 0
i = 0

# Iterate over strings while they are equal and index is not out of range: and compare char.lower() by char.lower()
while strings_are_equal and i < len(line1):
    # Check if char from string 1 is greater or less than char with same index from string 2
    if line1[i].lower() < line2[i].lower():
        print(-1)
        strings_are_equal = False
        continue
    elif line1[i].lower() > line2[i].lower():
        print(1)
        strings_are_equal = False
        continue
    else:
        i += 1

# If iteration was over and strings are equal - display corresponding message
if strings_are_equal:
    print(0)
