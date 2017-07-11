# Description of the problem can be found at http://codeforces.com/problemset/problem/822/B

x, y = map(int, input().split())
s = input()
t = input()

l_b_r = list()
b_c = None

for i in range(y):
    if i + x <= y:
        l_r = list()
        c_c = 0
        
        for j in range(x):
            if s[j] != t[j + i]:
                c_c += 1
                l_r.append(j + 1)
        
        if b_c == None or c_c < b_c:
            b_c = c_c
            l_b_r = l_r

print(b_c)
print(" ".join(str(x) for x in l_b_r))