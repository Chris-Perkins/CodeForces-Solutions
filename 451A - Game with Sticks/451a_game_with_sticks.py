# Description of the problem can be found at http://codeforces.com/problemset/problem/451/A

a, b = map(int, input().split())

if min(a, b) % 2 == 1:
	print("Akshat")
else:
	print("Malvika")