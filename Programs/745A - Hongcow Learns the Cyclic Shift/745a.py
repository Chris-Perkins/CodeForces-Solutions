# Description of the problem can be found at http://codeforces.com/problemset/problem/745/A

s = input()

s_s = set()
c = 0

while c != len(s):
    s_s.add(s[len(s) - c :] + s[:len(s) - c])
    c += 1

print(len(s_s))