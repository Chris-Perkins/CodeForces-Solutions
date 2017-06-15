# Description of the problem can be found at http://codeforces.com/problemset/problem/448/B

def get_d(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d

s1 = input()
s2 = input()

d1 = get_d(s1)

d_u = {}
for c in s2:
    if c in d1:
        if c not in d_u:
            d_u[c] = 0
        d_u[c] += 1
        
        d1[c] -= 1
        if d1[c] == 0:
            del d1[c]
    else:
        print("need tree")
        quit()
        
if len(d1.keys()) > 0:
    b = False
    
    i1 = 0
    i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        if(s1[i1] == s2[i2]):
            i1 += 1
            i2 += 1
            
            if i2 == len(s2):
                b = True
                break
        else:
            i1 += 1
    if b:
        print("automaton")
    else:
        print("both")
else:
    print("array")