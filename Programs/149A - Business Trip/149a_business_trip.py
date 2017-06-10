# Description of the problem can be found at http://codeforces.com/problemset/problem/149/A

w = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
s = 0
i = 0

while i < len(l) and s < w:
    s += l[i]
    i += 1

if s >= w:
    print(i)
else:
    print("-1")