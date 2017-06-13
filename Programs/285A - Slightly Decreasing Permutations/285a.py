# Description of the problem can be found at http://codeforces.com/problemset/problem/285/A

n, k = map(int, input().split())

l_n = [str(x) for x in range(1, n + 1)]

l_n = l_n[n : n - k - 1 : -1] + l_n[0 : n - k]
print(" ".join(l_n))