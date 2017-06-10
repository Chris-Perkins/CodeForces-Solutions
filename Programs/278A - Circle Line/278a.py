# Description of the problem can be found at http://codeforces.com/problemset/problem/278/A

n = int(input())
l_d = list(map(int, input().split()))
a, b = map(int, input().split())

if a > b:
    t = a
    a = b
    b = t

print(min(sum(l_d[a - 1 : b - 1]), sum(l_d[:a - 1]) + sum(l_d[b - 1:])))