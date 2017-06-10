# Description of the problem can be found at http://codeforces.com/problemset/problem/499/B

n, m = map(int, input().split())

d_w = {}
for _ in range(m):
	l_s = list(input().split())
	if len(l_s[1]) < len(l_s[0]):
		d_w[l_s[0]] = l_s[1]
	else:
		d_w[l_s[0]] = l_s[0]

l_w = list(input().split())

for w in l_w:
	print(d_w[w], end = " ")