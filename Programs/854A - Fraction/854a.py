# Description of the problem can be found at http://codeforces.com/problemset/problem/854/A

n = int(input())

if n & 1:
    a = n // 2
else:
    if n % 4 == 0:
        a = n // 2 - 1
    else:
        a = n // 2 - 2

b = n - a

print(a, b)