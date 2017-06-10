# Description of the problem can be found at http://codeforces.com/problemset/problem/279/B

n, t = map(int, input().split())
c = list(map(int, input().split()))

b = 0
c_t = 0
m = 0
for i in range(n):
    c_t += c[i]
    while c_t > t:
        c_t -= c[b]
        b += 1
    m = max(m, i - b + 1)
print(m)