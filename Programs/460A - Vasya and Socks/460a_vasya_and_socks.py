# Description of the problem can be found at http://codeforces.com/problemset/problem/460/A

n, m = map(int, input().split())
days = 0

# while we have more than 0 socks
while n > 0:
	days += 1
	# if we don't get replacement socks this day, subtract a pair
	if days % m != 0:
		n -= 1
		
print(days)