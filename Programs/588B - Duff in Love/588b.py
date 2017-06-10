# Description of the problem can be found at http://codeforces.com/problemset/problem/588/B

import math

n = int(input())

if n == 1:
    print(1)
    quit()
    
s_p = set()

while n % 2 == 0:
    s_p.add(2)
    n = n // 2;

i = 3
while i <= math.sqrt(n):
    while(n % i == 0):
        s_p.add(i)
        n //= i
    
    i += 2

if n > 2:
    s_p.add(n)

t = 1
for n in s_p:
    t *= n
print(t) 