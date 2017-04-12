# Description of the problem can be found at http://codeforces.com/problemset/problem/508/B

n = input()

c_p = -1
for i in range(len(n)):
    if int(n[i]) % 2 == 0:
        if int(n[len(n) - 1]) > int(n[i]):
            print(n[:i] + n[len(n) - 1] + n[i + 1:len(n) - 1] + n[i])
            quit()
        else:
            c_p = i
    
if c_p == -1:
    print(-1)
else:
    print(n[:c_p] + n[len(n) - 1] + n[c_p + 1:len(n) - 1] + n[c_p])
    