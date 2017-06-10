# Description of the problem can be found at http://codeforces.com/problemset/problem/80/A

p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

n, m = map(int, input().split())

print("YES" if p[p.index(n) + 1] == m else "NO")