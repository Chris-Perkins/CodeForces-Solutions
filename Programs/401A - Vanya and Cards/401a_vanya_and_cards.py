# Description of the problem can be found at http://codeforces.com/problemset/problem/401/A

n, x = map(int, input().split())
s_c = sum(list(map(int, input().split())))
print(abs(s_c) // x + (1 if s_c % x != 0 else 0))