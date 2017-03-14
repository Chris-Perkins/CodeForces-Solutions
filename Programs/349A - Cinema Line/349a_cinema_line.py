# Description of the problem can be found at http://codeforces.com/problemset/problem/349/A

n = int(input())
l_r = list(map(int, input().split()))
l_b = list([0, 0, 0])

for r in l_r:
    if r == 100:
        l_b[0] += 1
        if l_b[1] > 0:
            l_b[1] -= 1
            l_b[2] -= 1
        else:
            l_b[2] -= 3
    elif r == 50:
        l_b[1] += 1
        l_b[2] -= 1
    else:
        l_b[2] += 1
    
    if l_b[1] < 0 or l_b[2] < 0:
        print("NO")
        quit()

print("YES")