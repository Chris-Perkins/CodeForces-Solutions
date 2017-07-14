# Description of the problem can be found at http://codeforces.com/problemset/problem/722/A

n = int(input())
s = input().split(":")

if n == 12:
    c_t = list()
    for i, n_s in enumerate(s):
        if i == 0:
            s = ""
            s += ("0" if (n_s[0] > "1" and n_s[1] != "0") else ("1" if (n_s[1] == "0") else n_s[0]))
            s += ("1" if (n_s[1] > "2" and s[0] == "1") or (n_s[1] == "0" and s[0] == "0") else n_s[1])
            c_t.append(s)
        else:
            c_t.append(("0" if n_s[0] > "5" else n_s[0]) + n_s[1])
    print(":".join(c_t))
else:
    c_t = list()
    for i, n_s in enumerate(s):
        if i == 0:
            c_t.append(("0" if n_s[0] > "2" else n_s[0]) + ("1" if (n_s[0] == "2" and n_s[1] > "3") else n_s[1]))
        else:
            c_t.append(("0" if n_s[0] > "5" else n_s[0]) + n_s[1])
    print(":".join(c_t))