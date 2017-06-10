# Description of the problem can be found at http://codeforces.com/problemset/problem/712/B

d_s = {}
d_s["L"] = 0
d_s["R"] = 0
d_s["U"] = 0
d_s["D"] = 0

s = input()

for c in s:
    d_s[c] += 1
    
if abs(d_s["L"] - d_s["R"]) % 2 == abs(d_s["U"] - d_s["D"]) % 2:
    print((abs(d_s["L"] - d_s["R"]) + abs(d_s["U"] - d_s["D"])) // 2)
else:
    print(-1)