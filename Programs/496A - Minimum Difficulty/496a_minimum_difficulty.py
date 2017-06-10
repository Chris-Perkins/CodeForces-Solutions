# Description of the problem can be found at http://codeforces.com/problemset/problem/496/A


n = int(input())
l_n = list(map(int, input().split()))
m = l_n[n - 1] - l_n[0]
for i in range(1, n - 1):
    t_m = 0
    for j in range(1, n - 1):
        if j == i:
            t_m = max(t_m, l_n[j + 1] - l_n[j - 1])
        elif j + 1 != i:
            t_m = max(t_m, l_n[j + 1] - l_n[j])
    m = min(m, t_m)
print(m)