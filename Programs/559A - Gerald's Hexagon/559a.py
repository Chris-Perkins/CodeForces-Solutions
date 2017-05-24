# Description of the problem can be found at http://codeforces.com/problemset/problem/559/A

l_s = list(map(int, input().split()))
w = l_s[0] / 2
print((l_s[0] + l_s[1] + l_s[2]) ** 2 - l_s[0] ** 2 - l_s[2] ** 2 - l_s[4] ** 2)