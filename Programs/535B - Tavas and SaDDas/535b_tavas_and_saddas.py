# Description of the problem can be found at http://codeforces.com/problemset/problem/535/B

def get_places_before(n):
    if n // 10 != 0:
        return 2 + 2*(get_places_before(n // 10))
    else:
        return 0

n = int(input())

i1 = get_places_before(n)

c = 0
t_n = n
while t_n > 0:
    t_n //= 10
    c = max(1, c * 10)

i2 = 0
while n > 0:
    i2 *= 2
    i2 += 0 if n // c == 4 else 1
    n %= c
    c //= 10
    
print(i1 + i2 + 1)