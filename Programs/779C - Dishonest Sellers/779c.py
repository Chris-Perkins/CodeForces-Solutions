# Description of the problem can be found at http://codeforces.com/problemset/problem/779/C

n, k = map(int, input().split())

l_d = list(map(int, input().split()))
l_a = list(map(int, input().split()))

l_pd = list()
for i in range(n):
    l_pd.append([l_d[i] - l_a[i], i])

l_pd.sort()

t_b = 0
p = 0
for l in l_pd:
    if l[0] <= 0 or t_b < k:
        t_b += 1
        p += l_d[l[1]]
    else:
        p += l_a[l[1]]

print(p)