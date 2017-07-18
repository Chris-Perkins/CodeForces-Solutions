# Description of the problem can be found at http://codeforces.com/problemset/problem/510/B

[n, m]=[int(i) for i in input().split()]
visit=[[] for i in range(n)]

for i in range(n):
    s = input()
    for j in s:
        visit[i].append(ord(j))

def find(sr, st, en, pat):
    for i in range(st, en + 1, 1):
        if visit[sr][i] != pat:
            return 0
    return 1

for i in range(n):
    for j in range(m):
        k = j + 1
        while k < m and visit[i][j] == visit[i][k]:
            l = i + 1
            while l < n and visit[l][k] == visit[i][j]:
                if find(l, j, k, visit[i][j]):
                    print("Yes")
                    exit()
                l+=1
            k+=1
print('No')