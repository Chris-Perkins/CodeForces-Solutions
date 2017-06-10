# Description of the problem can be found at http://codeforces.com/problemset/problem/586/A

n = int(input())
l_p = list(map(int, input().split()))

t = 0
c_s = 2
for p in l_p:
    if p == 0:
        c_s += 1
    if p == 1:
        if c_s < 2:
            t += c_s
        c_s = 0
        t += 1

print(t)