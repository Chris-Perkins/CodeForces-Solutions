# Description of the problem can be found at http://codeforces.com/problemset/problem/462/A

n = int(input())
l_r = list(input() for _ in range(n))

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for i in range(n):
    for j in range(n):
        t = 0
        for k in range(4):
            if i + dx[k] >= 0 and i + dx[k] < n:
                if j + dy[k] >= 0 and j + dy[k] < n:       
                    if l_r[i + dx[k]][j + dy[k]] == 'o':
                        t += 1
        if t % 2 != 0:
            print("NO")
            quit()
print("YES")