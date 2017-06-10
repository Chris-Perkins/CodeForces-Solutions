# Description of the problem can be found at http://codeforces.com/problemset/problem/545/C

l_t = list()
for _ in range(int(input())):
    l_t.append(list(map(int, input().split())))

t = min(2, len(l_t))
i = 1

p_l = l_t[0][0]

while i < len(l_t) - 1:
    if l_t[i][0] - l_t[i][1] > p_l:
        p_l = l_t[i][0]
        t += 1
    elif l_t[i][0] + l_t[i][1] < l_t[i + 1][0]:
        p_l = l_t[i][0] + l_t[i][1]
        t += 1
    else:
        p_l = l_t[i][0]
    i += 1
print(t)