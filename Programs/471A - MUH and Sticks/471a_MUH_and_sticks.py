# Description of the problem can be found at http://codeforces.com/problemset/problem/471/A

l_s = list(map(int, input().split()))
s_s = set(l_s)

f = False
c = 0

for s in s_s:
    t_c = l_s.count(s)
    if t_c >= 4:
        f = True
        c = t_c
        break

if not f:
    print("Alien")
else:
    if len(s_s) == 3 or c == 5:
        print("Bear")
    else:
        print("Elephant")         