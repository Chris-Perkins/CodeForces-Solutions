# Description of the problem can be found at http://codeforces.com/problemset/problem/472/C

n = int(input())

l_n = list([input().split() for _ in range(n)])

o = list(map(int, input().split()))

l = "A"
for n in range(n):
    l_n[o[n] - 1].sort()
    
    if l_n[o[n] - 1][0] > l:
        l = l_n[o[n] - 1][0]
    elif l_n[o[n] - 1][1] > l:
        l = l_n[o[n] - 1][1]
    else:
        print("NO")
        exit()
print("YES")