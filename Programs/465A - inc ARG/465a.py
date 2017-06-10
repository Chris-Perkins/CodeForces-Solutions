# Description of the problem can be found at http://codeforces.com/problemset/problem/465/A

n = int(input())
s = input()

c = 1
t = 0
for c in s:
    t += 1
    if c == "0":
        c = 0
        break
print(t)