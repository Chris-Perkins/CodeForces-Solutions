# Description of the problem can be found at http://codeforces.com/problemset/problem/821/A

n = int(input())

l_r = list()
for _ in range(n):
    l_r.append([int(x) for x in input().split()])

l_s_c = list(set() for _ in range(n))
l_s_r = list(set() for _ in range(n))

for i in range(n):
    for j in range(n):
        l_s_c[j].add(l_r[i][j])
        l_s_r[i].add(l_r[i][j])

for i in range(n):
    for j in range(n):
        if l_r[i][j] == 1:
            continue

        f = False
        for v in l_s_c[j]:
            if l_r[i][j] - v in l_s_r[i]:
                f = True
                break
        if not f:
            print("No")
            quit()
print("Yes")