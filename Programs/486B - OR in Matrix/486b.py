# Description of the problem can be found at http://codeforces.com/problemset/problem/486/B

n, m = map(int, input().split())

l_n = list()

for _ in range(n):
    l_n.append(list(map(int, input().split())))

res = [[1 for _ in range(m)] for _ in range(n)]

for i in range(len(l_n)):
    for j in range(len(l_n[i])):
        if l_n[i][j] == 0:
            for k in range(n):
                res[k][j] = 0
            for l in range(m):
                res[i][l] = 0
                
for i in range(n):
    for j in range(m):
        if l_n[i][j]:
            if not(any(res[i]) or any(rr[j] for rr in res)):
                print("NO")
                quit()

print("YES")
for row in res:
    print(" ".join(str(x) for x in row))
                