# Description of the problem can be found at http://codeforces.com/problemset/problem/337/A


n, _ = map(int, input().split())
n -= 1

min_difference = None

puzzles = list(map(int, input().split()))
puzzles.sort()

for index in range(len(puzzles) - n):
	if min_difference == None or min_difference > puzzles[index + n] - puzzles[index]:
		min_difference = puzzles[index + n] - puzzles[index]
		
print(min_difference)