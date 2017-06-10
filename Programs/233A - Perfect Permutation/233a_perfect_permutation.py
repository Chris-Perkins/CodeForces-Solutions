# Description of the problem can be found at http://codeforces.com/problemset/problem/233/A

n = int(input())

if (n % 2 == 1):
    print(-1)
else:
    for i in range(1, n + 1):
        print((i + 1) if i % 2 == 1 else (i - 1), end = " ")