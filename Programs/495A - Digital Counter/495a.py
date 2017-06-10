# Description of the problem can be found at http://codeforces.com/problemset/problem/495/A

s = input()
t = 1

d_v = {}
d_v["0"] = 2
d_v["1"] = 7
d_v["2"] = 2
d_v["3"] = 3
d_v["4"] = 3
d_v["5"] = 4
d_v["6"] = 2
d_v["7"] = 5
d_v["8"] = 1
d_v["9"] = 2

for c in s:
    t *= d_v[c]
    
print(t)