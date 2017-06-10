# Description of the problem can be found at http://codeforces.com/problemset/problem/37/A

N = int(input())
l_l = list(map(int, input().split()))

d_l = {}
n = 0
m = 0

for l in l_l:
    if l in d_l:
        d_l[l] += 1
    else:
        n += 1
        d_l[l] = 1
    m = max(d_l[l], m)
    
print("%d %d" % (m, n))
            