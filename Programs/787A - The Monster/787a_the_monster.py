# Description of the problem can be found at http://codeforces.com/contest/787/problem/0
a, b = map(int, input().split())
c, d = map(int, input().split())

lcm = a * c

for i in range(10000):
    t1 = b + i * a
    x2 = (t1 - d) // c
    
    if t1 == d + x2*c and x2 >= 0:
        print(t1)
        quit()
print("-1")