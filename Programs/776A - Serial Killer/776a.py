# Description of the problem can be found at http://codeforces.com/problemset/problem/776/A

s_p = set(input().split())
print(" ".join(s_p))

for _ in range(int(input())):
    s1, s2 = input().split()
    s_p.remove(s1)
    s_p.add(s2)
    print(" ".join(s_p))