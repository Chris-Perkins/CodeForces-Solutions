# Description of the problem can be found at http://codeforces.com/problemset/problem/519/A

# init dict
d = {}
d["."] = 0
d["Q"] = 9
d["R"] = 5
d["B"] = 3
d["N"] = 3
d["P"] = 1
d["K"] = 0

t = 0

for _ in range(8):
    s = input()
    
    for c in s:
        if c in d:
            t += d[c]
        elif c.upper() in d:
            t -= d[c.upper()]

if t > 0:
    print("White")
elif t < 0:
    print("Black")
else:
    print("Draw")