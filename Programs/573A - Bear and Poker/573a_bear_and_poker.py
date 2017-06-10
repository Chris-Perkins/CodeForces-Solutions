# Description of the problem can be found at http://codeforces.com/problemset/problem/573/A

def f(x):
    while x % 2 == 0:
        x //= 2
    while x % 3 == 0:
        x //= 3
    return x

n = int(input())
l_n = [f(x) for x in list(map(int, input().split()))]
    
print("Yes" if min(l_n) == max(l_n) else "No")