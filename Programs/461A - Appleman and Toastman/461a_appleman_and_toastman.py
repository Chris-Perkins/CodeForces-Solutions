# Description of the problem can be found at http://codeforces.com/problemset/problem/461/A

_ = input()
l_i = list(map(int, input().split()))
l_i.sort()

s = sum(l_i)
t = sum(l_i)
a_s = 0

for i in range(len(l_i) - 1):
    t += s - a_s
    a_s += l_i[i]
    
print(t)