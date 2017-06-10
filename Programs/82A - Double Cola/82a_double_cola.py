# Description of the problem can be found at http://codeforces.com/problemset/problem/82/A

friends = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

cur_friend_count = 0
# multiplies by 2 each time they drink cola, so on the i(th) repeat,
# there are len*multiplier in this section
multiplier = 1

n = int(input())

while(cur_friend_count + len(friends) * multiplier < n):
	cur_friend_count += len(friends) * multiplier
	multiplier *= 2

print(friends[((n - cur_friend_count - 1) // multiplier)])