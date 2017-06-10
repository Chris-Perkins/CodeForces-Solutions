# Description of the problem can be found at http://codeforces.com/problemset/problem/427/A

_ = input()
e = list(map(int, input().split()))
t = 0
c = 0

for o in e:
    if o == -1:
        if t == 0:
            c += 1
        else:
            t -= 1
    else:
        t += o

print(c)