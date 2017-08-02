# Description of the problem can be found at http://codeforces.com/problemset/problem/340/A

x, y, a, b = map(int, input().split())

lcm = 1
c_i = 1
while c_i <= x or c_i <= y:
    if x % c_i == 0 and y % c_i == 0:
        lcm= c_i
    c_i += 1
lcm = (x * y) // lcm
print(int(b // lcm - (a - 1) // lcm))