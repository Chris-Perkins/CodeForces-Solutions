# Description of the problem can be found at http://codeforces.com/problemset/problem/361/A

n, k = map(int, input().split())
v = k - (n - 1)

t = list()
for i in range(n):
    t.append([(1 if i + c + 1 != n else v) for c in range(n)])

for n in t:
    print(" ".join(str(x) for x in n))