# Description of the problem can be found at http://codeforces.com/problemset/problem/545/A

n = int(input())

l_c = list()
l_g = list()

for i in range(n):
    l_c.append(list(map(int, input().split())))

for i in range(n):
    f = True
    for j in range(n):
        if l_c[i][j] == 1 or l_c[i][j] == 3:
            f = False
            break
    if f:
        l_g.append(str(i + 1))
print(len(l_g))
print(" ".join(l_g))