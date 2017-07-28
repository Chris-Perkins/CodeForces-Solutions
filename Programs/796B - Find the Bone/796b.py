# Description of the problem can be found at http://codeforces.com/problemset/problem/796/B

n, m, k = map(int, input().split())

s = set()
for n in list(map(int, input().split())):
    s.add(n)

b = 1
for _ in range(k):
    if b in s:
        print(b)
        quit()
    
    x1, x2 = map(int, input().split())
    if x1 == b:
        b = x2
    elif x2 == b:
        b = x1

print(b)