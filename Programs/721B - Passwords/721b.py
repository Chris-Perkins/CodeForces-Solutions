# Description of the problem can be found at http://codeforces.com/problemset/problem/721/B

n, k = map(int, input().split())


l_l = list()
for _ in range(n):
    l_l.append(len(input()))

p = len(input())

h_t = 0
l_t = 0
for l in l_l:
    if l < p:
        h_t += 1
        l_t += 1
    elif l == p:
        h_t += 1
l_t += 1
print("%d %d" % (l_t + ((l_t - 1) // k) * 5, h_t + ((h_t - 1) // k) * 5))