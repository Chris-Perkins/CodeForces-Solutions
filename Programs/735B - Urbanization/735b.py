# Description of the problem can be found at http://codeforces.com/problemset/problem/735/B

n, m, o = map(int, input().split())

l_n = list(map(float, input().split()))
l_n.sort(reverse = True)

w = [0] * 2
i = 0

if m > o:
    o, m = m, o

while i < m + o:
    if i >= m:
        w[1] += l_n[i]
    else:
        w[0] += l_n[i]
    i += 1

print(w[0] / m + w[1] / o)