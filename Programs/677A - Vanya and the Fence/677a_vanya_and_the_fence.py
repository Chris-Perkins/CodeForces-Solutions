# Description of the problem can be found at http://codeforces.com/problemset/problem/677/A

_, h = map(int, input().split())
a = list(map(int, input().split()))
w = 0

for h_f in a:
    if h_f > h:
        w += 1
    w += 1

print(w)