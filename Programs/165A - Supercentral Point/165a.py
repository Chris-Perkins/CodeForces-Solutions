# Description of the problem can be found at http://codeforces.com/problemset/problem/165/A

n = int(input())
l_c = list()

for _ in range(n):
    l_c.append(list(map(int, input().split())))

t = 0

for i in range(n):
    s_i = set()
    
    for j in range(n):
        if i == j:
            pass
        elif l_c[i][0] == l_c[j][0]:
            if l_c[i][1] > l_c[j][1]:
                s_i.add("D")
            elif l_c[i][1] < l_c[j][1]:
                s_i.add("U")
        elif l_c[i][1] == l_c[j][1]:
            if l_c[i][0] > l_c[j][0]:
                s_i.add("L")
            elif l_c[i][0] < l_c[j][0]:
                s_i.add("R")
    
    if len(s_i) == 4:
        t += 1

print(t)