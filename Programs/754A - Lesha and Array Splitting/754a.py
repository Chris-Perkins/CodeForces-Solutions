# Description of the problem can be found at http://codeforces.com/problemset/problem/754/A

x = int(input())
l_i = list(map(int, input().split()))

l_s = list()
c_l = list()
c_s = 0

c_l.append(1)
for i in range(len(l_i)):
    if l_i[i] + c_s == 0:
        if len(c_l) != 0 and c_s != 0:
            c_l.append(i)
            l_s.append(c_l)
            c_l = list()
            c_l.append(i + 1)
            c_s = 0
    c_s += l_i[i]
c_l.append(len(l_i))
l_s.append(c_l)

if c_s == 0 and len(c_l) != 0:
    print("NO")
else:
    print("YES")
    print(len(l_s))
    for l in l_s:
        print(" ".join(str(x) for x in l))