# Description of the problem can be found at 

n = int(input())
l_n = list(map(int, input().split()))

d = {}
t = 0
for n in l_n:
    while n in d and n > 0:
        n -= 1
    d[n] = ""
    t += n

print(t)