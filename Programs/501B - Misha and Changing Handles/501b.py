# Description of the problem can be found at http://codeforces.com/problemset/problem/501/B

d_n = {}

n = int(input())

for _ in range(n):
    x, y = input().split()
    
    if x in d_n:
        d_n[y] = d_n[x]
        del d_n[x]
    else:
        d_n[y] = x

print(len(d_n))
for key in d_n:
    print("%s %s" % (d_n[key], key))