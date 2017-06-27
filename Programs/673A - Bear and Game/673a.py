# Description of the problem can be found at http://codeforces.com/problemset/problem/673/A

n = int(input())

l_n = list(x for x in map(int, input().split()))
l_n.append(90)
t = 0
for n in l_n:
    if t + 15 < n:
        print(t + 15)
        quit()
    else:
        t = n
        
print(t)