# Description of the problem can be found at http://codeforces.com/problemset/gymProblem/101028/E

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

T = int(input())

for _ in range(T):
    _ = input()
    l_p = list(map(int, input().split()))
    
    t_p = 0
    gcd_t = 0
    for p in l_p:
        t_p += p
        gcd_t = gcd(p, gcd_t)
    
    print("%d %d" % (gcd_t, t_p // gcd_t))