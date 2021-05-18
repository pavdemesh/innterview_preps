# https://codeforces.com/contest/381/problem/A

"""
Sereja and Dima

Sereja and Dima play a game. The rules of the game are very simple. The players have n cards in a row.
Each card contains a number, all numbers on the cards are distinct. The players take turns, Sereja moves first.
During his turn a player can take one card: either the leftmost card in a row, or the rightmost one.
The game ends when there is no more cards.
The player who has the maximum sum of numbers on his cards by the end of the game, wins.

Sereja and Dima are being greedy. Each of them chooses the card with the larger number during his move.

Inna is a friend of Sereja and Dima. She knows which strategy the guys are using and wants to determine the final score.
Given the initial state of the game. Help her.

Input
The first line contains integer n (1 <= n <= 1000) — the number of cards on the table.
The second line contains space-separated numbers on the cards from left to right.
The numbers on the cards are distinct integers from 1 to 1000.

Output
On a single line, print two integers.
The number of Sereja's points at the end of the game, followed by the number of Dima's points at the end of the game.

Examples
input
4
4 1 2 10
output
12 5
"""

# Get n - total number of cards
total_cards = int(input())

# Initialize list of cards and get input
cards = list(map(int, input().split()))

# Initialize total points for Sereja and Dima
total_s = 0
total_d = 0
cur_max = 0

# Initialize left and right cursors (indices)
left = 0
right = len(cards) - 1

for i in range(total_cards):
    # Determine current maximum of 2 numbers:
    if cards[left] >= cards[right]:
        cur_max = cards[left]   # update current maximum
        left += 1   # update left index
    else:
        cur_max = cards[right]  # update current maximum
        right -= 1  # update right index
    # Update total points for Sereja or Dima
    if i % 2 == 0:
        total_s += cur_max
    else:
        total_d += cur_max

print(total_s, total_d)
