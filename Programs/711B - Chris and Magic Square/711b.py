# Description of the problem can be found at http://codeforces.com/problemset/problem/711/B

n = int(input())
l_c = [list() for _ in range(n)]

s_l = None
j = None
k = None

if n == 1:
    print(1)
    quit()

for i in range(n):
    l_c[i] = list(map(int, input().split()))
    if 0 in l_c[i]:
        j = i
        k = l_c[i].index(0)
    else:
        if s_l:
            if s_l != sum(l_c[i]):
                print(-1)
                quit()
        else:
            s_l = sum(l_c[i])

l_c[j][k] = s_l - sum(l_c[j])

if l_c[j][k] <= 0:
    print(-1)
    quit()

for c in range(n):
    if sum(l_c[r][c] for r in range(n)) != s_l:
        print(-1)
        quit()

if not (sum(l_c[r][r] for r in range(n)) == s_l == sum(l_c[r][n - 1 - r] for r in range(n))):
    print(-1)
    quit()
else:
    print(l_c[j][k])