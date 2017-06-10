# Description of the problem can be found at http://codeforces.com/problemset/problem/567/A

n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    j, k = None, None
    if i > 0:
        j = abs(l[i] - l[i - 1])
    if i < n - 1:
        k = abs(l[i + 1] - l[i])
    if j == None:
        print(k, end = " ")
    elif k == None:
        print(j, end = " ")
    else:
        print(min(j, k), end = " ")
    print(max(l[i] - l[0], l[len(l) - 1] - l[i]))