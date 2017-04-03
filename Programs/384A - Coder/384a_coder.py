# Description of the problem can be found at http://codeforces.com/problemset/problem/384/A

n = int(input())

t = 0
l_o = list()
for i in range(n):
    l_c = list()
    for j in range(n):
        if (i % 2 + j) % 2 == 0:
            t += 1
            l_c.append("C")
        else:
            l_c.append(".")
    l_o.append(l_c)
    
print(t)
print("\n".join("".join(l_c) for l_c in l_o))