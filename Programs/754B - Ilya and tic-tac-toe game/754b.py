# Description of the problem can be found at http://codeforces.com/problemset/problem/754/B

d_x = [ 0,  1, 1,  1]
d_y = [-1, -1, 1,  0]

l_p = list()
for _ in range(4):
    l_p.append(list(input()))

for x in range(4):
    for y in range(4):
        if l_p[y][x] != "o":
            for i in range(len(d_x)):
                if (y + d_y[i] * 2 < 4 and y + d_y[i] * 2 >= 0 and
                    x + d_x[i] * 2 < 4 and x + d_x[i] * 2 >= 0):
                    b = True
                    c_p = 0
                    for j in range(3):
                        if l_p[y + d_y[i] * j][x + d_x[i] * j] == "." and c_p == 0:
                            c_p = 1
                        elif (l_p[y + d_y[i] * j][x + d_x[i] * j] == "o" or
                            (c_p == 1 and l_p[y + d_y[i] * j][x + d_x[i] * j] == ".")):
                            b = False
                            break
                    
                    if b:
                        print("YES")
                        quit()
                else:
                    pass
print("NO")