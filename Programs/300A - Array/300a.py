# Description of the problem can be found at http://codeforces.com/problemset/problem/300/A

n = int(input())
l_i = list(map(int, input().split()))

c_n = None
l_n = set()
l_p = set()
l_0 = set()

for i in l_i:
    if i < 0:
        if i not in l_n and i not in l_p:
            if len(l_n) != 1:
                l_n.add(i)
            elif not c_n:
                c_n = i
            elif i != c_n:
                l_p.add(c_n)
                l_p.add(i)
                c_n = None
    elif i > 0:
        l_p.add(i)
    else:
        l_0.add(i)

print(str(len(l_n)) + " " + " ".join(str(x) for x in l_n))
print(str(len(l_p)) + " " + " ".join(str(x) for x in l_p))
print(str(len(l_0) + (1 if c_n else 0)) + " 0" + ("" if not c_n else " %d" % c_n))