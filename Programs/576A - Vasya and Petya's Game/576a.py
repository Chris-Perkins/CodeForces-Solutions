# Description of the problem can be found at http://codeforces.com/problemset/problem/576/A

n = int(input())

s_p = set(i for i in range(2, n + 1))

for i in range(2, (int(n ** (1/2))) + 1):
    if i in s_p:
        for j in range(2, n // i + 1):
            if i * j in s_p:
                s_p.remove(i * j)

l_o = list()

for i in s_p:
    c_e = i
    
    while i <= n:
        l_o.append(i)
        i *= c_e

print(len(l_o))
print(" ".join(str(x) for x in l_o))