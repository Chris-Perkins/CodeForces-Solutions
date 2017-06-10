# Description of the problem can be found at http://codeforces.com/problemset/problem/723/B

n = int(input())

s = input()
i_p = False
l = 0
m_l = 0
t_i_p = 0
for c in s:
    if c == "(":
        m_l = max(m_l, l)
        l = 0
        i_p = True
    elif c == ")":
        if l != 0:
            t_i_p += 1
        l = 0
        i_p = False
    elif c == "_":
        if i_p and l != 0:
            t_i_p += 1
        else:
            m_l = max(m_l, l)
        l = 0
    else:
        l += 1

m_l = max(m_l, l)
print("%d %d" % (m_l, t_i_p))