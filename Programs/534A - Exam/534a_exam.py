# Description of the problem can be found at http://codeforces.com/problemset/problem/534/A

n = int(input())

l_o = list()
l_e = list()

for i in range(1, n + 1):
    if i % 2 == 0:
        l_e.append(i)
    else:
        l_o.append(i)
        
l_e.sort(reverse = True)
l_o.sort(reverse = True)
l_o.extend(l_e)

if n >= 2 and abs(l_o[n  - len(l_e)] - l_o[n - len(l_e) - 1]) <= 1:
    l_o.remove(l_o[n - 1])

print(len(l_o))
print(" ".join(str(x) for x in l_o))