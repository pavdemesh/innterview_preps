# https://codeforces.com/contest/677/problem/A

"""
Vanya and his friends are walking along the fence of height h and they do not want the guard to notice them.
In order to achieve this the height of each of the friends should not exceed h.
If the height of some person is greater than h he can bend down and then he surely won't be noticed by the guard.
The height of the i-th person is equal to ai.

Consider the width of the person walking as usual to be equal to 1, while the width of the bent person is equal to 2.
Friends want to talk to each other while walking, so they would like to walk in a single row.
What is the minimum width of the road, such that friends can walk in a row and remain unattended by the guard?

Input:
The first line of the input contains two integers n and h (1 <= n <= 1000, 1 <= h <= 1000):
The number of friends and the height of the fence, respectively.

The second line contains n integers ai (1 <= ai <= 2h), the i-th of them is equal to the height of the i-th person.

Output
Print a single integer — the minimum possible valid width of the road.

Example
Input line 1:   3 7
Input line 2:   4 5 14
Output:         4
"""

# Get input
num_friends, height_fence = (map(int, input().split()))
list_of_heights = list(map(int, input().split()))

# List comprehension: make list of 1s and 2s for each height of the friends. Use sum() on this list.
required_width = sum([1 if x <= height_fence else 2 for x in list_of_heights])

# Display results
print(required_width)
