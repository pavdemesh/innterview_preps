# https://codeforces.com/contest/236/problem/A

"""
A. Boy or Girl

Those days, many boys use beautiful girls' photos as avatars in forums.
So it is pretty hard to tell the gender of a user at the first glance.
Last year, our hero went to a forum and had a nice chat with a beauty (he thought so).
After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man!
Our hero is very sad and he is too tired to love again now.
So he came up with a way to recognize users' genders by their user names.

This is his method:
if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female.

You are given the string that denotes the user name, help our hero to determine the gender of this user by his method.

Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name.
This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes),
otherwise, print "IGNORE HIM!" (without the quotes).
"""

# Get input
user_name = input()

# Determine distinct chars using set functionality
# unique_chars = set(user_name)
# This will return a set of unique chars. Then count length of set if even - girl, if odd - boy.

# Determine unique chars "manually"
# Create empty string to hold unique chars
unique_chars = ""
# Iterate over chars in user_name. If char is not present in unique_chars, add that char to unique_chars
for char in user_name:
    if char in unique_chars:
        continue
    else:
        unique_chars += char

# Determine boy or girl based on len of unique_chars and display result
print("IGNORE HIM!" if len(unique_chars) % 2 == 1 else "CHAT WITH HER!")
