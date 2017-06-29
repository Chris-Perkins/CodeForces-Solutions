# Description of the problem can be found at http://codeforces.com/problemset/problem/330/B

n, m = map(int, input().split())

s_e = set(i for i in range(n))

for _ in range(m):
    x, y = map(int, input().split())
    
    s_e.discard(y - 1)
    s_e.discard(x - 1)

c = s_e.pop()
print(n - 1)
for i in range(n):
    if i != c:
        print(" ".join(str(x) for x in [i + 1, c + 1]))