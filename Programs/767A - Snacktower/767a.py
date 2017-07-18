# Description of the problem can be found at http://codeforces.com/problemset/problem/767/A

n = int(input())
t = [0] * n

n = list(map(int, input().split()))
l_s = list()
i = 0
while len(t) != 0:
    t[n[i] - 1] = 1
    a = list()
    while len(t) != 0 and t[len(t) - 1] == 1:
        a.append(len(t))
        del t[len(t) - 1]
    print(" ".join(str(x) for x in a))
    i += 1