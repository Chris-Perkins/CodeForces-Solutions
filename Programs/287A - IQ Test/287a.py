# Description of the problem can be found at http://codeforces.com/problemset/problem/287/A

l_l = list([input() for _ in range(4)])

dx = [ 0,  0,  1,  1]
dy = [ 0, -1, -1,  0]

for i in range(3):
    for j in range(3):
        t = 0
        for z in range(4):
            t += (-1 if l_l[i + dy[z]][j + dx[z]] == "#" else 1)
        
        if abs(t) >= 2:
            print("YES")
            quit()
print("NO")