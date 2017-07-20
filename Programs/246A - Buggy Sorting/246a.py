# Description of the problem can be found at http://codeforces.com/problemset/problem/246/A

n = int(input())

if n <= 2:
    print(-1)
else:
    print("2 " * (n - 1) + "1")