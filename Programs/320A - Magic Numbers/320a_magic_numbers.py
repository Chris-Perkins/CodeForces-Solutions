# Description of the problem can be found at http://codeforces.com/problemset/problem/320/A

s = input()

c_i = 0
f = False
while c_i < len(s):
    if len(s) - c_i >= 3 and s[c_i:c_i + 3] == "144":
        c_i += 3
    elif len(s) - c_i >= 2 and s[c_i:c_i + 2] == "14":
        c_i += 2
    elif len(s) - c_i >= 1 and s[c_i:c_i + 1] == "1":
        c_i += 1
    else:
        f = True
        break

if f:
    print("NO")
else:
    print("YES")