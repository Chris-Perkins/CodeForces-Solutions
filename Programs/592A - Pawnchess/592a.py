# Description of the problem can be found at http://codeforces.com/problemset/problem/592/A

l_w = [9] * 8
l_b = [9] * 8

for y in range(8):
    i = 0
    for c in input():
        if c == "W":
            if l_b[i] == 9 and l_w[i] == 9:
                l_w[i] = y
            l_b[i] = 10
        elif c == "B":
            l_b[i] = 7 - y
        i += 1

min_w = min(l_w)
min_b = min(l_b)

if min_w > min_b:
    print("B")
else:
    print("A")