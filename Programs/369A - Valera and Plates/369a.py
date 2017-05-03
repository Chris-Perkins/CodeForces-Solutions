# Description of the problem can be found at http://codeforces.com/problemset/problem/369/A

n, m, k = map(int, input().split())
l_d = list(map(int, input().split()))

t = 0
for d in l_d:
    if d == 2:
        if k > 0:
            k -= 1
        else:
            if m > 0:
                m -= 1
            else:
                t += 1
    else:
        if m > 0:
            m -= 1
        else:
            t += 1

print(t)