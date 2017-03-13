# Description of the problem can be found at http://codeforces.com/problemset/problem/758/A

_ = input()
l_w = list(map(int, input().split()))
m = max(l_w)
t = 0

for w in l_w:
    t += m - w

print(t)