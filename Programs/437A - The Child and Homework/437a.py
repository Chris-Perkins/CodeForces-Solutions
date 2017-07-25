# Description of the problem can be found at http://codeforces.com/problemset/problem/437/A

max_i = -1
max_l = "A"
min_i = -1
min_l = 100
c = "E"

l_s = list()
for _ in range(4):
    l_s.append(input())

l_s.sort(key = lambda x: len(x))

if (len(l_s[0]) - 2)  * 2 <= len(l_s[1]) - 2:
    if len(l_s[3]) - 2 >= (len(l_s[2]) - 2) * 2:
        print("C")
    else:
        print(l_s[0][0])
elif len(l_s[3]) - 2 >= (len(l_s[2]) - 2) * 2:
    print(l_s[3][0])
else:
    print("C")