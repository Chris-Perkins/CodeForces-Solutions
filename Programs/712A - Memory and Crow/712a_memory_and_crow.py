# Description of the problem can be found at http://codeforces.com/problemset/problem/712/A

n = int(input())
l_n = list(map(int, input().split()))

c_s = 0
for i in range(len(l_n)):
    l_n[len(l_n) - i - 1] += c_s
    c_s = -c_s
    c_s += l_n[len(l_n) - i - 1]

print(" ".join(str(x) for x in l_n))