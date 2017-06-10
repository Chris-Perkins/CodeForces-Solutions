# Description of the problem can be found at http://codeforces.com/problemset/problem/805/B

n = int(input())

for i in range(n):
    if i % 4 < 2:
        print("a", end = "")
    else:
        print("b", end = "")