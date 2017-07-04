# Description of the problem can be found at http://codeforces.com/problemset/problem/761/B

n, L = map(int, input().split())
l_x = list(map(int, input().split()))
l_x.sort()
l_y = list(map(int, input().split()))

for i in range(L):
    for j in range(n):
        l_y[j] = (l_y[j] + 1) % L

    l_y = sorted(l_y)

    if sorted(l_y) == l_x:
        print("YES")
        quit()

print("NO")