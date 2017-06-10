# Description of the problem can be found at http://codeforces.com/problemset/problem/757/A

s = input()
d_c = {}
for c in s:
    if c not in d_c:
        d_c[c] = 1
    else:
        d_c[c] += 1

if 'B' in d_c and 'u' in d_c and 'l' in d_c and 'b' in d_c and 'a' in d_c and 's' in d_c and 'r' in d_c:
    print(min([d_c['B'], d_c['u'] // 2, d_c['l'], d_c['b'], d_c['a'] // 2, d_c['s'], d_c['r']]))
else:
    print(0)