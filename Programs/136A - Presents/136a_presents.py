# Description of the problem can be found at http://codeforces.com/problemset/problem/136/A

num_friends = int(input())

presents = []
for _ in range(num_friends):
	presents.append(0)

friends = list(map(int, input().split()))

for index in range(len(friends)):
	# Could I have printed here?
	# Maybe, but then readability goes down.
	# Therefore, I won't think about this more.
	presents[friends[index] - 1] = index
	
for gifter in presents:
	print(gifter + 1, end = " " if gifter != presents[len(presents) - 1] else "")