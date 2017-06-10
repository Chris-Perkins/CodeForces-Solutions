# Description of the problem can be found at http://codeforces.com/problemset/problem/155/A

_ = input()
scores = [int(x) for x in input().split()]
a = 0
w_p = scores[0]
b_p = scores[0]

for s in scores:
    if s > b_p:
        a += 1
        b_p = s
    elif s < w_p:
        a += 1
        w_p = s

print(a)