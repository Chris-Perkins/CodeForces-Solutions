# Description of the problem can be found at http://codeforces.com/problemset/problem/493/B

n = int(input())

p = 0
s1 = list()
s2 = list()
l = 0

for s in list(input() for _ in range(n)):
    p += int(s)
    (s1 if int(s) > 0 else s2).append(abs(int(s)))
    l = 1 if int(s) > 0 else -1

if p != 0:
    print("first" if p > 0 else "second")
    quit()

if s1 != s2:
    print("first" if s1 > s2 else "second")
else:
    print("first" if l == 1 else "second")