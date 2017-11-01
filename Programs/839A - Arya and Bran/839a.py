# Description of the problem can be found at http://codeforces.com/problemset/problem/839/A

n, k = map(int, input().split())
list_candies = list(map(int, input().split()))

i, r = 0, 0
for c in list_candies:
    r += c
    i += 1
    k -= min(8, r)
    r -= min(8, r)
    if k <= 0:
        print(i)
        quit()
print(-1)