# Description of the problem can be found at http://codeforces.com/problemset/problem/352/A

_ = int(input())

l_n = input().split()
d_n = {}
d_n["0"] = 0
d_n["5"] = 0

for n in l_n:
    d_n[n] += 1

if d_n["0"] == 0:
    print("-1")
elif d_n["5"] < 9:
    print("0")
else:
    print("%s%s" % ("5"*(d_n["5"] - d_n["5"] % 9), "0"*d_n["0"]))