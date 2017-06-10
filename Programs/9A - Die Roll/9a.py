# Description of the problem can be found at http://codeforces.com/problemset/problem/9/A

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = 7 - max(map(int, input().split()))
print("%d/%d" % (n // gcd(n, 6), 6 // gcd(n, 6)))