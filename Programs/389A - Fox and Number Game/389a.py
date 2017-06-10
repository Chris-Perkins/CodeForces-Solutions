# Description of the problem can be found at http://codeforces.com/problemset/problem/389/A

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b % a, a)
    
n = int(input())
l_n = list(map(int, input().split()))

g = gcd(l_n[0], l_n[1])
for i in range(2, n):
    g = gcd(g, l_n[i])
    
print(g * n)