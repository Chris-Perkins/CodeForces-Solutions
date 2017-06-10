# Description of the problem can be found at http://codeforces.com/problemset/problem/43/C

n = int(input())

l_n = list(map(int, input().split()))

a_t = [0]*3

for t_n in l_n:
    a_t[t_n % 3] += 1

print(a_t[0] // 2 + min(a_t[1], a_t[2]))