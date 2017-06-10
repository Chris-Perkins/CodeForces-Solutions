# Description of the problem can be found at http://codeforces.com/problemset/problem/672/A

n = int(input())

l_n = list()

for t_n in range(1, 371):
    t_l_n = list()
    while t_n != 0:
        t_l_n.append(t_n % 10)
        t_n //= 10
    t_l_n.reverse()
    l_n.extend(t_l_n)

print(l_n[n - 1])
