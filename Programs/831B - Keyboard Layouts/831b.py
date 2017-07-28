# Description of the problem can be found at http://codeforces.com/problemset/problem/831/B

d = {}
s = input()
s2 = input()
for (i, c) in enumerate(s):
    d[c] = s2[i]

w = input()
for c in w:
    if c.lower() in d:
        print(d[c.lower()].lower() if c != c.upper() else d[c.lower()].upper(), end = "")
    else:
        print(c, end = "")