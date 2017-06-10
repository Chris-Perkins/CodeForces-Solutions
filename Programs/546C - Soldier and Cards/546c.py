# Description of the problem can be found at http://codeforces.com/problemset/problem/546/C

n = list(map(int, input().split()))

l_1 = list(map(int, input().split()))[1:]
l_2 = list(map(int, input().split()))[1:]

l_1c = l_1.copy()
l_2c = l_2.copy()

t = 0
while len(l_1c) != 0 and len(l_2c) != 0:
    if l_1c[0] == l_2c[0]:
        l_1c.append(l_1c[0])
        l_2c.append(l_2c[0])
    elif l_1c[0] > l_2c[0]:
        l_1c.append(l_2c[0])
        l_1c.append(l_1c[0])
    else:
        l_2c.append(l_1c[0])
        l_2c.append(l_2c[0])
    
    del l_1c[0]
    del l_2c[0]
    
    t += 1
    if t > 10000:
        print(-1)
        quit()

print("%d %d" % (t, 2 if len(l_1c) == 0 else 1))