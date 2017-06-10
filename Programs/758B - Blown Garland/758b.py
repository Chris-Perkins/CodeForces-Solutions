# Description of the problem can be found at http://codeforces.com/problemset/problem/758/B

g = input()

l_c = [""] * 4

for i in range(len(g)):
    if g[i] != "!":
        l_c[i % 4] = g[i]

d_c = {}
d_c["R"] = 0
d_c["G"] = 0
d_c["B"] = 0
d_c["Y"] = 0

for i in range(len(g)):
    if g[i] == "!":
        d_c[l_c[i % 4]] += 1
            
print("%d %d %d %d" % (d_c["R"], d_c["B"], d_c["Y"], d_c["G"]))