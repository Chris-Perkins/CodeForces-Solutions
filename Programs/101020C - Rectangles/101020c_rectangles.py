# Description of the problem can be found at http://codeforces.com/problemset/gymProblem/101020/C

T = int(input())

for _ in range(T):
    n = int(input())
    
    a_a = [0]*100
    a = 0
    
    for _ in range(n):
        i, j, k = map(int, input().split())
        
        for l in range(i, j):
            if k > a_a[l]:
                a += k - a_a[l]
                a_a[l] = k
    
    print(a)