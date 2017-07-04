# Description of the problem can be found at http://codeforces.com/problemset/problem/389/C

n = int(input())
l_b = list(map(int, input().split()))
l_b.sort()
p = 0

s_d = list()

while len(l_b) > 0:
    t = 0

    for i, b in enumerate(l_b):
        if b >= t:
            s_d.append(i)
            t += 1

    for i in s_d[::-1]:
        del l_b[i]

    s_d = list()

    p += 1

print(p)