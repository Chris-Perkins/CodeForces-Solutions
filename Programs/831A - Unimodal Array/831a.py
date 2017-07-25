# Description of the problem can be found at http://codeforces.com/problemset/problem/831/A

n = int(input())

c = False
k = 0
p = 0

l_n = list(map(int, input().split()))
for n in l_n:
    if not c and n == p:
        k = n
        c = True
    if not c and n < p:
        c = True
    elif c and n > p:
        print("NO")
        quit()
    elif c and n == p and n != k:
        print("NO")
        quit()
    p = n
print("YES")