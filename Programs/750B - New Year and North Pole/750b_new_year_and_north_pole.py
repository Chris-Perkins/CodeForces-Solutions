# Description of the problem can be found at http://codeforces.com/problemset/problem/750/B

n = int(input())
p = 0

for _ in range(n):
    i = input().split()
    if i[1][0] not in set(["W", "E"]):
        if i[1][0] == "N":
            if p != 0 and p >= int(i[0]):
                p -= int(i[0])
            else:
                print("NO")
                quit()
        else:
            if p != 20000 and 20000 >= p + int(i[0]):
                p += int(i[0])
            else:
                print("NO")
                quit()
    else:
        if p == 0 or p == 20000:
            print("NO")
            quit()

if p == 0:
    print("YES")
else:
    print("NO")