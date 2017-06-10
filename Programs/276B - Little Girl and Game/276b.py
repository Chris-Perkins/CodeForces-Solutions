# Description of the problem can be found at http://codeforces.com/problemset/problem/276/B

s = input()

d_e = {}
n_o = 0

for c in s:
    if c not in d_e:
        d_e[c] = 0
    d_e[c] += 1
    if (d_e[c] % 2 == 1):
        n_o += 1
    else:
        n_o -= 1
if n_o == 0:
    print("First")
elif n_o % 2 == 1:
    print("First")
else:
    print("Second")    