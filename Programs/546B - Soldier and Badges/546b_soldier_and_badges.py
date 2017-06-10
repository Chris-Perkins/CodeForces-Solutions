# Description of the problem can be found at http://codeforces.com/problemset/problem/546/B

n = int(input())
l_n = list(map(int, input().split()))
f_a = [0]*6000

for t_n in l_n:
    f_a[t_n] += 1

t = 0
c_n = 0
for i in range(6000):
    t += c_n
    
    if f_a[i] > 1:
        c_n += f_a[i] - 1
    elif f_a[i] == 0 and c_n > 0:
        c_n -= 1
print(t)