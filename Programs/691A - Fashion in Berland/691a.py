# Description of the problem can be found at http://codeforces.com/problemset/problem/691/A

n = int(input())

l_b = list(map(int, input().split()))
if sum(l_b) == max(1, n - 1):
    print("YES")
else:
    print("NO")