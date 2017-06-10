# Description of the problem can be found at http://codeforces.com/problemset/problem/560/B

def b_f(l_a, i, l_r):
    if(i == 2):
        return True

    for j in range(2):
        if (l_a[i][0] <= l_r[j] and l_a[i][1] <= l_r[(j + 1) % 2]):
            if(b_f(l_a, i + 1, [l_r[j], l_r[(j + 1) % 2] - l_a[i][1]])):
                return True
        if (l_a[i][1] <= l_r[j] and l_a[i][0] <= l_r[(j + 1) % 2]):
            if(b_f(l_a, i + 1, [l_r[j], l_r[(j + 1) % 2] - l_a[i][0]])):
                return True
    
    return False
    
a1, a2 = map(int, input().split())

l_s = list()
l_s.append(list(map(int, input().split())))
l_s.append(list(map(int, input().split())))

if b_f(l_s, 0, [a1, a2]):
    print("YES")
else:
    print("NO")