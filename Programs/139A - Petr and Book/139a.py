# Description of the problem can be found at http://codeforces.com/problemset/problem/139/A

p = int(input())

l_n = list(map(int, input().split()))
n_s = sum(l_n)

while p > n_s:
    p -= n_s

while p > 0:
        for i in range(len(l_n)):
            if l_n[i] >= p:
                print(i + 1)
                quit()
            p -= l_n[i]