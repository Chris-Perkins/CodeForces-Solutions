# Description of the problem can be found at http://codeforces.com/problemset/problem/760/A

m, d = map(int, input().split())

l_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

t_d = l_m[m - 1]

print((d + t_d - 1) // 7 + (1 if (d + t_d - 1) % 7 != 0 else 0))