# Description of the problem can be found at http://codeforces.com/problemset/problem/474/A

d = {}
s = "qwertyuiopasdfghjkl;zxcvbnm,./"

a = 1 if input() == "L" else -1
i = input()
for c in i:
    if c in d:
        i = d[c]
    else:
        i = s.index(c)
        d[c] = i
    print(s[i + a], end = "")