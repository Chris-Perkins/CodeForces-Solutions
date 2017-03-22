# Description of the problem can be found at http://codeforces.com/problemset/problem/431/A

l_a = list(map(int, input().split()))
s = input()
t_c = 0

for c in s:
    t_c += l_a[int(c) - 1]

print(t_c)