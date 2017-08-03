# Description of the problem can be found at http://codeforces.com/problemset/problem/834/A

d = {"v":  0, "<": 1, "^": 2, ">": 3}
f1, f2 = input().split()
s = int(input())

x1 = (d[f1] + s) % 4 == d[f2]
x2 = (d[f1] - s) % 4 == d[f2]
if x1 and x2:
    print("undefined")
elif x1:
    print("cw")
else:
    print("ccw")
