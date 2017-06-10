# Description of the problem can be found at http://codeforces.com/problemset/problem/567/B

n = int(input())
l_p = list()

s_e = set()
p_e = 0
for _ in range(n):
    l_t = input().split()
    l_p.append(l_t)
    if int(l_t[0] == "-" and int(l_t[1]) in s_e):
        p_e -= 1
        s_e.remove(int(l_t[1]))
    elif l_t[0] == "+":
        p_e += 1
        s_e.add(int(l_t[1]))

c_p = p_e
m_p = c_p
for l_t in l_p[::-1]:
    if l_t[0] == "-":
        c_p += 1
    else:
        c_p -= 1
    m_p = max(m_p, c_p)

print(m_p)