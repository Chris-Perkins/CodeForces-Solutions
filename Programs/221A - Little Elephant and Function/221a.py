# Description of the problem can be found at http://codeforces.com/problemset/problem/221/A

n = int(input())
l_x = [n] + [(i + 1) for i in range(n - 1)]

print(" ".join(str(x) for x in l_x))