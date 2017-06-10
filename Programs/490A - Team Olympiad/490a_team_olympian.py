# Description of the problem can be found at http://codeforces.com/problemset/problem/490/A

l_p = list()
l_m = list()
l_e = list()

_ = input()
l_s = list(map(int, input().split()))

for i in range(len(l_s)):
    if l_s[i] == 1:
        l_p.append(i + 1)
    elif l_s[i] == 2:
        l_m.append(i + 1)
    else:
        l_e.append(i + 1)

n = min(len(l_p), len(l_m), len(l_e))
print(n)

for i in range(n):
    print("%d %d %d" % (l_p[i], l_m[i], l_e[i]))