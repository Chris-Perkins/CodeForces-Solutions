# Description of the problem can be found at http://codeforces.com/problemset/problem/478/A

s_c = sum(int(x) for x in input().split())
print((s_c // 5) if s_c % 5 == 0 and s_c != 0 else -1)