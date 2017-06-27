# Description of the problem can be found at http://codeforces.com/problemset/problem/277/A

n, m = tuple(map(int, input().split()))
lst = [[]]
for _ in range(n):
    lst.append(list(map(int, input().split()))[1:])
uses = [0] * (n + 1)
cnt = cnt_n = 0

def dfs(i, m):
    uses[i] = m
    for x in lst[i]:
        for j in range(1, n + 1):
            if uses[j] == 0 and x in lst[j]:
                dfs(j, m)

if lst == [[]] * (n + 1):
    print(n)
else:
    for i in range(1, n + 1):
        if uses[i] == 0:
            cnt += 1
            dfs(i, cnt)
    print(cnt - 1)