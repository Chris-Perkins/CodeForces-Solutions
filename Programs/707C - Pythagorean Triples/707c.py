# Description of the problem can be found at http://codeforces.com/problemset/problem/707/C

n = int(input())

b = n // 2

if n < 3:
    print(-1)
elif(n % 2 == 1):
    print(2 * b * (b + 1), 2 * b * (b+1) + 1)
else:
    print(b * b - 1, b * b + 1)