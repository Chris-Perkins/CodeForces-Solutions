# Description of the problem can be found at http://codeforces.com/problemset/problem/710/A

s = input()

m = set(["DL", "DR", "D", "UL", "UR", "U", "L", "R"])
if s[0] == "a":
    m.discard("DL")
    m.discard("UL")
    m.discard("L")
elif s[0] == "h":
    m.discard("DR")
    m.discard("UR")
    m.discard("R")
if s[1] == "8":
    m.discard("U")
    m.discard("UR")
    m.discard("UL")
elif s[1] == "1":
    m.discard("D")
    m.discard("DL")
    m.discard("DR")

print(len(m))