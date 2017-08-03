# Description of the problem can be found at http://codeforces.com/problemset/problem/835/B

k = int(input())

x = [0] * 10
for c in input():
    c = int(c)
    k -= c
    x[c] += 1
t = 0
i = 0
while k > 0 and i != 9:
    c = min(k // (9 - i) + (1 if k % (9 - i) != 0 else 0), x[i])
    k -= c * (9 - i)
    i += 1
    t += c
print(t)