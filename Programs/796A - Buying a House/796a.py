# Description of the problem can be found at http://codeforces.com/problemset/problem/796/A

n, m, k = map(int, input().split())
l_p = list(map(int, input().split()))

m -= 1
i = 1

while i < n:
    if m + i < n:
        if l_p[m + i] <= k and l_p[m + i] != 0:
            print(i * 10)
            quit()
    if m - i >= 0:
        if l_p[m - i] <= k and l_p[m - i] != 0:
            print(i * 10)
            quit()
            
    i += 1