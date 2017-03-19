# Description of the problem can be found at http://codeforces.com/problemset/problem/556/A

_ = input()
s = input()
a_n = [0]*2

for c in s:
    a_n[int(c)] += 1

print(abs(a_n[1] - a_n[0]))