# Description of the problem can be found at http://codeforces.com/problemset/problem/478/C

r, g, b = map(int, input().split())
z = min(r + g + b, 3 * min(r + b, g + b, g + r))
print(z // 3)