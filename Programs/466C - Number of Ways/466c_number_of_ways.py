# Description of the problem can be found at http://codeforces.com/problemset/problem/466/C

n = int(input())
l_n = list(map(int, input().split()))
a, s = 0, sum(l_n)

if s % 3 == 0:
    p1 = s // 3
    p2 = s - p1
    s = c = 0
    for i in range(n - 1):
        s += l_n[i]
        if s == p2:
            a += c
        if s == p1:
            c += 1
print(a)