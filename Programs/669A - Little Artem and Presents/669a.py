# Description of the rpoblem can be found at http://codeforces.com/problemset/problem/669/A

n = int(input())

print((n // 3) * 2 + (1 if n % 3 > 0 else 0))