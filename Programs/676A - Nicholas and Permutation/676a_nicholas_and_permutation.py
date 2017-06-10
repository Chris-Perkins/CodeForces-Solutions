# Description of the problem can be found at http://codeforces.com/problemset/problem/676/A

n = int(input())
l_n = list(map(int, input().split()))

max_i = l_n.index(max(l_n))
min_i = l_n.index(min(l_n))

print(max(max_i, min_i, n - min_i - 1, n - max_i - 1))