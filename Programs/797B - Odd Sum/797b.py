# Description of the problem can be found at http://codeforces.com/contest/797/problem/B

n = int(input())
l_n = list(map(int, input().split()))

l_o = list()
s = 0
for n in l_n:
    if n % 2 == 0:
        if abs(n) == n:
            s += n
    else:
        l_o.append(n)


l_o.sort()

m_s = s
t_s = s
m_n_o = None
n_i = -1
for i in range(len(l_o)):
    if abs(l_o[i]) != l_o[i]:
        m_n_o = l_o[i]
        n_i = i
    else:
        break

if len(l_o) - n_i - 1 == 0:
    print(s + m_n_o)
elif (len(l_o) - n_i - 1) % 2 == 0:
    print(max(s + sum(l_o[n_i + 2:]), 
              (s + sum(l_o[n_i + 1:]) + (m_n_o if m_n_o else int(-1e10)))))
else:
    print(s + sum(l_o[n_i + 1:]))