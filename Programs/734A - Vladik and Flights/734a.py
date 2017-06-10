# Description of the problem can be found at http://codeforces.com/problemset/problem/743/A

n, a, b = map(int, input().split())
l_a = input()

if l_a[b - 1] == l_a[a - 1]:
    print(0)
else:
    print(1)