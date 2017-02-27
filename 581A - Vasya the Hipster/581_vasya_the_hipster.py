# Description of the problem can be found at http://codeforces.com/problemset/problem/581/A

a, b = map(int, input().split())
days = min(a, b)
print(days)
print(((a + b) // 2) - days)