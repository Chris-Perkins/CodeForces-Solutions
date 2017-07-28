# Description of the problem can be found at http://codeforces.com/problemset/problem/801/B

x, y = input(), input()
l_z = list()

for i in range(len(x)):
    if y[i] > x[i]:
        print("-1")
        quit()
    elif y[i] < x[i]:
        l_z.append(y[i])
    else:
        l_z.append(x[i])

print("".join(l_z))