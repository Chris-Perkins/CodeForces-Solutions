# Description of the problem can be found at http://codeforces.com/problemset/problem/678/A

n, k = map(int, input().split())

x = n // k + 1
print(x * k)