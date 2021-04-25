# https://codeforces.com/contest/734/problem/A

"""
Anton likes to play chess, and so does his friend Danik. Once they have played n games in a row.
For each game it's known who was the winner — Anton or Danik. None of the games ended with a tie.
Now Anton wonders, who won more games, he or Danik? Help him determine this.

Input:
The first line of the input contains a single integer n (1<=n<=100_000) — the number of games played.
The second line contains a string s, consisting of n uppercase letters 'A' and 'D' — outcome of each of the games.
The i-th character of the string is equal to 'A' if the Anton won the i-th game and 'D' if Danik won the i-th game.

Output:
If Anton won more games than Danik, print "Anton" (without quotes) in the only line of the output.
If Danik won more games than Anton, print "Danik" (without quotes) in the only line of the output.
If Anton and Danik won the same number of games, print "Friendship" (without quotes).
"""

# Get input
total_games = int(input())
string_with_results = input()

# Goal is a more 'manual' and low-level solution
# Create counter to track wins by Anton and Danik
wins_anton = 0
wins_danik = 0

# Iterate over string, check letters one-by-one and update corresponding counters
for i in range(len(string_with_results)):
    if string_with_results[i] == "A":
        wins_anton += 1
    else:    # if not "A" then it must be "D"
        wins_danik += 1

# Compare counters and display results
if wins_danik > wins_anton:
    print("Danik")
elif wins_danik < wins_anton:
    print("Anton")
else:
    print("Friendship")
