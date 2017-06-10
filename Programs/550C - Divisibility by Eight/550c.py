# Description of the problem can be found at http://codeforces.com/problemset/problem/550/C

s = input()

a = "NO"
for i in[str(i) for i in range(1000) if i % 8 == 0]:
    t = -1
    
    for c in i:
        t = s.find(c, t + 1)
        
        if t == -1:
            break
        
    if t != -1:
        a = 'YES\n' + i
print(a)