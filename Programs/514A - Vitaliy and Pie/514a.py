# Description of the problem can be found at http://codeforces.com/problemset/problem/525/A

n = int(input())
l_c = input()

t = 0
d_k = {}

for i in range(n * 2 - 2):
    if i % 2 == 0:
        if l_c[i] not in d_k:
            d_k[l_c[i]] = 1
        else:
            d_k[l_c[i]] += 1
    else:
        if l_c[i].lower() in d_k and d_k[l_c[i].lower()] > 0:
            d_k[l_c[i].lower()] -= 1
        else:
            t += 1
            
print(t)