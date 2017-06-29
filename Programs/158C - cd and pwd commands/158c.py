# Description of the problem can be found at http://codeforces.com/problemset/problem/158/C

n = int(input())

l_d = list()
x = 0

for _ in range(n):
    l_c = list(input().split())
    
    if l_c[0] == "pwd":
        print("/" + "".join(l_d[:x]))
    else:
        for c in l_c[1].split("/"):
            if c == "..":
                x -= 1
            elif len(c) != 0:
                if len(l_d) > x:
                    l_d[x] = c + "/"
                else:
                    l_d.append(c + "/")
                x += 1
            else:
                x = 0