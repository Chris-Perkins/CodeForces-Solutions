# Description of the problem can be found at http://codeforces.com/problemset/problem/544/A

n = int(input())
s = input()

s_s = set()
l_i = list()

for (i, c) in enumerate(s):
    if len(l_i) != n:
        if c not in s_s:
            if len(l_i) != 0:
                l_i[len(l_i) - 1][1] = i
            l_i.append([i, len(s)])
            
            s_s.add(c)
    else:
        break

if len(l_i) != n:
    print("NO")
else:
    print("YES\n" + "\n".join(s[l_i[i][0]:l_i[i][1]] for i in range(n)))