# Description of the problem can be found at http://codeforces.com/problemset/problem/465/B

n = int(input())
l_r = input().split()

t = -1
p_r = False

for r in l_r:
    if r == "1":
        t += 1
        if not p_r:
            t += 1
        p_r = True
    else:
        p_r = False

print(t if t != -1 else 0)