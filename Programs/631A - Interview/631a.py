# Description of the problem can  be found at http://codeforces.com/problemset/problem/631/A

n = int(input())

l_i1 = list(map(int, input().split()))
l_i2 = list(map(int, input().split()))

o1 = 0
o2 = 0

for i in range(n):
    o1 |= l_i1[i]
    o2 |= l_i2[i]
    
print(o1 + o2)