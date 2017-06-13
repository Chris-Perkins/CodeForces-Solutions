# Description of the problem can be found at http://codeforces.com/problemset/problem/591/B

n, m = map(int, input().split())
s = list(input())

d_c = {}

for c in range(26):
    d_c[chr(ord("a") + c)] = chr(ord("a") + c)

for _ in range(m):
    x, y = input().split()
    if x != y:
        d_c[x], d_c[y] = d_c[y], d_c[x]
        
d_c = {v: k for k, v in d_c.items()}
print("".join(d_c[c] for c in s))