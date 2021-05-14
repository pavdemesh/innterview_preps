# https://codeforces.com/contest/281/problem/A

"""
Word Capitalization

Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.
Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters.
The length of the word will not exceed 10^3.
Output
Output the given word after capitalization.

Input: ApPLe    --->>>     Output: ApPLe
"""

text = input()

# Check if the first letter is already capitalized # I.e. its numerical value is in range (65, 90)
if 65 <= ord(text[0]) <= 90:
    # If yes - do nothing
    pass
else:
    # Take numerical value of the lower case letter and subtract 32 and convert back to char
    first_letter_capital = chr(ord(text[0]) - 32)
    # Replace first letter in text with its capitalized version
    text = first_letter_capital + text[1:]

# Display result
print(text)
