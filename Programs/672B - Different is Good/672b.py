# Description of the problem can be found at http://codeforces.com/problemset/problem/672/B

n = int(input())
s = input()

if len(s) > 26:
    print(-1)
else:
    print(n - len(set(c for c in s)))