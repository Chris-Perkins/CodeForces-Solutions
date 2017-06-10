# Description of the problem can be found at http://codeforces.com/problemset/problem/265/B

n = int(input())

c_h = 0
t = 0
for i in range(n):
    h = int(input())
    if h >= c_h:
        t += h - c_h
        c_h = h
    else:
        t += c_h - h
        c_h = h
    t += 2

# minus one as we don't just on last tree
t -= 1
print(t)