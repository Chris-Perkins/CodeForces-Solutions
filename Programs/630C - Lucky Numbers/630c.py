# Description of the problem can be found at http://codeforces.com/problemset/problem/630/C

n = int(input())

c_e = 1
c_s = 0

for i in range(1, n + 1):
    c_s += c_e * 2
    c_e *= 2
    
print(c_s)