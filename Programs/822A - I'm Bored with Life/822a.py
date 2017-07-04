# Description of the problem can be found at http://codeforces.com/problemset/problem/822/A

def fact(A):
    t = 1

    while A > 1:
        t *= A
        A -= 1

    return t

A, B = map(int, input().split())

if A == B:
    print(fact(A))
elif A > B:
    print(fact(B))
else:
    print(fact(A))