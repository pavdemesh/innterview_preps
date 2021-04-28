# https://codeforces.com/contest/734/problem/B

"""
Recently Anton found a box with digits in his room. 
There are k2 digits 2, k3 digits 3, k5 digits 5 and k6 digits 6.
Anton's favorite integers are 32 and 256. He decided to compose this integers from digits he has. 
He wants to make the sum of these integers as large as possible. Help him solve this task!

Each digit can be used no more than once, 
i.e. the composed integers should contain no more than k2 digits 2, k3 digits 3 and so on. 
Of course, unused digits are not counted in the sum.

Input:
The only line of the input contains four integers k2, k3, k5 and k6:
— the number of digits 2, 3, 5 and 6 respectively (0 <= k2,k3,k5,k6 ≤ 5·10^6).

Output:
Print one integer — maximum possible sum of Anton's favorite integers 
that can be composed using digits from the box.
"""

# Get input
freqs = list(map(int, input().split()))
# Create list of corresponding digits
digs = [2, 3, 5, 6]

# Map digits to their frequencies using a dictionary comprehension
digits = {digs[i]: freqs[i] for i in range(4)}

# Initialize and set maximum possible sum to 0
max_sum = 0

# Determine how many 256s can be composed by finding min() of available 2s, 5s, and 6s
count_256 = min(digits[2], digits[5], digits[6])

# Update max_sum by 256 * min() of available 2s, 5s, 6s
max_sum += (256 * count_256)

# Update the count of available 2s, cause they are needed to construct 32
digits[2] -= count_256

# Determine how many 32s can be composed by finding min() of available 2s and 3s
count_32 = min(digits[3], digits[2])

# Update max_sum by 32 * min() of available 2s and 3s
max_sum += (32 * count_32)

# Display result
print(max_sum)
