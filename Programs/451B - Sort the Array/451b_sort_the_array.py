# Description of the problem can be found at http://codeforces.com/problemset/problem/451/B

_ = input()
a_n = list(map(int, input().split()))
l = 0
h = 0
s = True

for i in range(1, len(a_n)):
    if s:
        if a_n[i] > a_n[i - 1]:
            if a_n[l] != a_n[h]:
                if a_n[i] < a_n[l]:
                    print("no")
                    quit()
                else:
                    s = False
            else:
                h = i
                l = i
        else:
            h += 1
    elif a_n[i] < a_n[i - 1]:
        print("no")
        quit()

if l > 0 and a_n[h] < a_n[l - 1]:
    print("no")
else:
    print("yes")
    print("%d %d" % (l + 1, h + 1))