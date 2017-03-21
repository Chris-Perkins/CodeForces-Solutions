# Description of the problem can be found at http://codeforces.com/problemset/problem/441/A

n, m = map(int, input().split())

l_s = list()
t = 0

for i in range(n):
    l_i = list(map(int, input().split()))
    
    for p in l_i[1:]:
        if m > p:
            t += 1
            l_s.append(str(i + 1))
            break
            
print(t)
print(" ".join(l_s))