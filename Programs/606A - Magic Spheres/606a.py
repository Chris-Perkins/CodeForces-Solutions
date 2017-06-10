# Description of the problem can be found at http://codeforces.com/problemset/problem/606/A

l_c_h = list(map(int, input().split()))
l_c_n = list(map(int, input().split()))

e = 0
for i in range(3):
    if l_c_h[i] - l_c_n[i] >= 0:
        e += (l_c_h[i] - l_c_n[i]) // 2
    else:
        e += l_c_h[i] - l_c_n[i]
        
print("YES" if e >= 0 else "NO")