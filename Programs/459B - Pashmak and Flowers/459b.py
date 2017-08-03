# Description of the problem can be found at http://codeforces.com/problemset/problem/459/B

n = int(input())
d = {}
l, h = None, None

for i in list(map(int, input().split())):
    if i not in d:
        d[i] = 0
    d[i] += 1
    
    if l == None:
        l, h = i, i
    else:
        l = min(i, l)
        h = max(i, h)

print(h - l, end = " ")
if l != h:
    print(d[l] * d[h])
else:
    print(d[l] * (d[l] - 1) // 2)